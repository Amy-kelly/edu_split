from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from homeapp.models import Carousel, Nav
from homeapp.serializers import CarouselModelSerializer,NavModelSerializer


class CarouselListAPIView(ListAPIView):
    queryset = Carousel.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = CarouselModelSerializer

class NavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_delete=False)
    serializer_class = NavModelSerializer