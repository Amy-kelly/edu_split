from django.urls import path

from courseapp import views

urlpatterns = [
    path("category/", views.CourseCategoryListAPIView.as_view()),
    path("course/", views.CourseListAPIView.as_view()),
    path("course_filter/", views.CourseFilterListAPIView.as_view()),
    path("course_detail/", views.CourseDetailAPIView.as_view()),
    path("course_detail/<str:id>/", views.CourseDetailAPIView.as_view()),
]