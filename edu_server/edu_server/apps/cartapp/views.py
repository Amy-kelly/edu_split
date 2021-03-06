import logging
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from courseapp.models import Course, CourseExpire
from edu_server.settings import constants

log = logging.getLogger("django")

class CartViewSet(ViewSet):

    permission_classes = [IsAuthenticated]

    # 将商品加入购物车的业务逻辑
    def add_cart(self,request):
        course_id = request.data.get("course_id")
        user_id = request.user.id
        select = True
        expire = 0
        try:
            Course.objects.get(is_show=True,id=course_id)
        except Course.DoesNotExist:
            return Response({"message":"抱歉，您所选中得课程不存在"},status=status.HTTP_400_BAD_REQUEST)
        try:
            redis_connection = get_redis_connection("cart")
            pipeline = redis_connection.pipeline()
            pipeline.multi()
            pipeline.hset("cart_%s" % user_id,course_id,expire)
            pipeline.sadd("selected_%s" % user_id, course_id)
            # 执行
            pipeline.execute()
            #显示购物车的数目
            course_length = redis_connection.hlen('cart_%s' % user_id)
        except:
            log.error("购物车信息数据存储失败")
            return Response({"message":"参数有误，添加购物车失败"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"课程添加购物车成功","course_length":course_length})

    #展示购物车信息
    def cart_list(self,request):
        user_id = request.user.id
        redis_connection = get_redis_connection("cart")
        cart_list_bytes = redis_connection.hgetall('cart_%s' % user_id)
        select_list_bytes = redis_connection.smembers("selected_%s" % user_id)
        # print(cart_list_bytes)
        # print("*****")
        # print(select_list_bytes)
        data = []
        for course_id_byte,expire_id_byte in cart_list_bytes.items():
            course_id = int(course_id_byte)
            expire_id = int(expire_id_byte)
            print(expire_id,type(expire_id))
            try:
                course = Course.objects.get(is_show=True,is_delete=False,pk=course_id)
                print(course)
            except Course.DoesNotExist:
                continue
            data.append({
                "selected":True if course_id_byte in select_list_bytes else False,
                "course_img":constants.IMAGE_SRC + course.course_img.url,
                "name":course.name,
                "id":course.id,
                "expire_id":expire_id,
                # "price":course.real_price(),
                "expire_list":course.expire_list,
                "real_price":course.real_expire_price(expire_id)
            })
        return Response(data)

    #切换购物车商品状态
    def change_select(self,request):
        user_id = request.user.id
        selected = request.data.get("selected")
        course_id = request.data.get("course_id")
        try:
            Course.objects.get(is_show=True,is_delete=False,id=course_id)
        except Course.DoesNotExist:
            return Response({"message":"当前商品不存在"},status=status.HTTP_400_BAD_REQUEST)

        redis_connection = get_redis_connection("cart")
        if selected:
            redis_connection.sadd("selected_%s" % user_id,course_id)
        else:
            redis_connection.srem("selected_%s" % user_id,course_id)
        return Response({"message":"商品状态切换成功"})

    def change_expire(self, request):
        """改变redis中课程的有效期"""
        user_id = request.user.id
        expire_id = request.data.get("expire_id")
        course_id = request.data.get("course_id")
        print(course_id, expire_id)

        try:
            course = Course.objects.get(is_show=True, is_delete=False, id=course_id)
            # 如果前端传递来的有效期选项  如果不是0  则修改课程对应的有效期
            if expire_id > 0:
                expire_item = CourseExpire.objects.filter(is_show=True, is_delete=False, id=expire_id)
                if not expire_item:
                    raise Course.DoesNotExist()
        except Course.DoesNotExist:
            return Response({"message": "课程信息不存在"}, status=status.HTTP_400_BAD_REQUEST)

        connection = get_redis_connection("cart")
        connection.hset("cart_%s" % user_id, course_id, expire_id)
        real_price = course.real_expire_price(expire_id)
        return Response({"message": "切换有效期成功","real_price":real_price})

    #删除指定商品
    def del_course(self,request):
        user_id = request.user.id
        course_id = request.query_params.get("course_id")
        print(course_id)
        try:
            course = Course.objects.get(is_show=True,is_delete=False,id=course_id)
        except Course.DoesNotExist:
            return Response({"message":"当前商品不存在"},status=status.HTTP_400_BAD_REQUEST)
        redis_connection = get_redis_connection("cart")
        pipe = redis_connection.pipeline()
        pipe.multi()
        pipe.hdel('cart_%s' % user_id,course_id)
        pipe.srem("selected_%s" % user_id,course_id)
        pipe.execute()
        return Response({"message":"删除成功"})

    def get_select_course(self, request):
        """
        获取购物车中已勾选的商品  返回前端所需的数据
        """

        user_id = request.user.id
        redis_connection = get_redis_connection("cart")

        # 获取当前登录用户的购车中所有的商品
        cart_list = redis_connection.hgetall("cart_%s" % user_id)
        select_list = redis_connection.smembers("selected_%s" % user_id)

        total_price = 0  # 商品总价
        data = []

        for course_id_byte, expire_id_byte in cart_list.items():
            course_id = int(course_id_byte)
            expire_id = int(expire_id_byte)
            print(course_id, expire_id)

            # 判断商品id是否在已勾选的的列表中
            if course_id_byte in select_list:
                try:
                    # 获取到的所有的课程信息
                    course = Course.objects.get(is_show=True, is_delete=False, pk=course_id)
                except Course.DoesNotExist:
                    continue
                # 如果有效期的id大于0  则需要计算商品的价格  id不大于0则代表永久有效 需要默认值
                original_price = course.price
                expire_text = "永久有效"

                try:
                    if expire_id > 0:
                        course_expire = CourseExpire.objects.get(id=expire_id)
                        # 对应有效期的价格
                        original_price = course_expire.price
                        expire_text = course_expire.expire_text
                except CourseExpire.DoesNotExist:
                    pass

                # 根据已勾选的商品的对应有效期的价格去计算勾选商品的最终价格
                real_expire_price = course.real_expire_price(expire_id)

                # 将购物车所需的信息返回
                data.append({
                    "course_img": constants.IMAGE_SRC + course.course_img.url,
                    "name": course.name,
                    "id": course.id,
                    "expire_text": expire_text,
                    # 活动、有效期计算完成后的  真实价格
                    "real_price": "%.2f" % float(real_expire_price),
                    # 原价
                    "price": original_price,
                    "discount_name": course.discount_name,
                })

                # 商品叠加后的总价
                total_price += float(real_expire_price)

        return Response({"course_list": data, "total_price": total_price, "message": '获取成功'})



# class CartDeleteAPIView(APIView):
#     def delete(self,request,*args,**kwargs):
#         user_id = request.user.id
#         course_id = kwargs.get("id")
#         # print(course_id)
#         try:
#             course = Course.objects.get(is_show=True, is_delete=False, id=course_id)
#             # print(course)
#         except Course.DoesNotExist:
#             return Response({"message": "当前商品不存在"}, status=status.HTTP_400_BAD_REQUEST)
#         redis_connection = get_redis_connection("cart")
#         if course:
#             # Course.objects.get(id=course_id).update(is_show=False, is_delete=True)
#             redis_connection.hdel("cart_%s" % user_id, course_id)
#             course_obj = redis_connection.smembers("cart_%s" % user_id)
#             print(course_obj)
#             # data = self.cart_list(request)
#         else:
#             return Response({"message": "当前商品不存在"}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(course_obj)



