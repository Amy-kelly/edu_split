import logging
from rest_framework.request import Request
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from courseapp.models import Course
from edu_server.settings import constants
from utils.response import MyResponse

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
            # print(course_id)
            try:
                course = Course.objects.get(is_show=True,is_delete=False,pk=course_id)
                print(course)
            except Course.DoesNotExist:
                continue
            data.append({
                "selected":True if course_id_byte in select_list_bytes else False,
                # "course_img":constants.IMAGE_SRC + course.course_img,
                "name":course.name,
                "id":course.id,
                "expire_id":expire_id,
                "price":course.price
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
            redis_connection.add("selected_%s" % user_id,course_id)
        else:
            redis_connection.srem("selected_%s" % user_id,course_id)
        return Response({"message":"商品状态切换成功"})

    #删除指定商品
    # def del_course(self,request):
    #     user_id = request.user.id
    #     course_id = request.data.get("course_id")
    #     try:
    #         course = Course.objects.get(is_show=True,is_delete=False,id=course_id)
    #     except Course.DoesNotExist:
    #         return Response({"message":"当前商品不存在"},status=status.HTTP_400_BAD_REQUEST)
    #     redis_connection = get_redis_connection("cart")
    #     if course:
    #         redis_connection.srem("selected_%s" % user_id, course_id)
    #     else:
    #         return Response({"message": "当前商品不存在"}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({"message":"删除成功"})

class CartDeleteAPIView(APIView):
    def delete(self,request,*args,**kwargs):
        user_id = request.user.id
        course_id = kwargs.get("id")
        # print(course_id)
        try:
            course = Course.objects.get(is_show=True, is_delete=False, id=course_id)
            # print(course)
        except Course.DoesNotExist:
            return Response({"message": "当前商品不存在"}, status=status.HTTP_400_BAD_REQUEST)
        redis_connection = get_redis_connection("cart")
        if course:
            # Course.objects.get(id=course_id).update(is_show=False, is_delete=True)
            redis_connection.hdel("cart_%s" % user_id, course_id)
            course_obj = redis_connection.smembers("cart_%s" % user_id)
            print(course_obj)
            # data = self.cart_list(request)
        else:
            return Response({"message": "当前商品不存在"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(course_obj)



