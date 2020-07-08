from django.urls import path

from homeapp import views

urlpatterns = [
    path("carousel/", views.CarouselListAPIView.as_view()),
    path("nav/", views.NavListAPIView.as_view()),
]