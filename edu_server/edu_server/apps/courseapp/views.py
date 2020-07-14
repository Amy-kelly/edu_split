from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from courseapp.models import CourseCategory, Course
from courseapp.pagination import CoursePageNumber
from courseapp.serializer import CourseCategorySerializer, CourseModelSerializer,CommentModelSerializer


# 课程分类信息查询
from utils.response import MyResponse


class CourseCategoryListAPIView(ListAPIView):
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseCategorySerializer


# 课程列表查询
class CourseListAPIView(ListAPIView):
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer


# 根据条件查询课程
class CourseFilterListAPIView(ListAPIView):
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer

    # 根据不同的分类id查询不同的课程
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("course_category",)
    # 排序
    ordering_fields = ("id", "students", "price")
    # 分页   只能有一个
    pagination_class = CoursePageNumber

#根据课程名称查询单个课程详情
# class CourseDetailAPIView(APIView):
#     def get(self,request,*args,**kwargs):
#         cour_id = kwargs.get("id")
#         if cour_id:
#
#             cour_obj = Course.objects.filter(pk=cour_id).first()
#             cour_ser = CourseModelSerializer(cour_obj).data
#             return Response({
#                 "status":200,
#                 "msg":"ok",
#                 "results":cour_ser
#             })


        # return Response({
        #     "status": 400,
        #     "msg": "error",
        # })
#
class CourseDetailAPIView(RetrieveModelMixin,GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    lookup_field = "id"
    def get(self,request,*args,**kwargs):
        cour_id = kwargs.get("id")
        print(cour_id)
        if cour_id:
            cour_obj = self.retrieve(request,*args,**kwargs)
            return Response({
                "status": 200,
                "msg":"ok",
                "results":cour_obj.data
            })

class CommentGenericAPIView(ListModelMixin,
                             CreateModelMixin,
                             RetrieveModelMixin,
                             UpdateModelMixin,
                             DestroyModelMixin,
                             GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CommentModelSerializer
    def get(self,request,*args,**kwargs):
        cour_id = kwargs.get("pk")
        if cour_id:
            course = self.retrieve(request,*args,**kwargs)
            return MyResponse(status.HTTP_200_OK,True,results=course.data)
        else:
            courses = self.list(request,*args,**kwargs)
            return MyResponse(status.HTTP_200_OK, True, results=courses.data)

    def patch(self,request,*args,**kwargs):
        cour_obj = self.partial_update(request,*args,**kwargs)
        return MyResponse(status.HTTP_200_OK, True, results=cour_obj.data)


