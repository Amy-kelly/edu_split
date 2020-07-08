from rest_framework import serializers

from homeapp.models import Carousel, Nav


class CarouselModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ("img", 'link')

class NavModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ("title","link","position")
