from django.db import models

# Create your models here.
#轮播图模型
from homeapp.BaseModel import BaseModel


class Carousel(BaseModel):
    img = models.ImageField(upload_to="carousel", max_length=255, verbose_name="轮播图图片")
    title = models.CharField(max_length=200, verbose_name="轮播图标题")
    link = models.CharField(max_length=300, verbose_name="图片链接")

    class Meta:
        db_table = "cms_carousel"
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

#导航栏
class Nav(BaseModel):
    position_option = (
        (1, "顶部导航"),
        (2, "底部导航"),
    )
    title = models.CharField(max_length=200, verbose_name="导航标题")
    link = models.CharField(max_length=300, verbose_name="导航链接")
    position = models.IntegerField(choices=position_option, default=1, verbose_name="导航位置")
    is_site = models.BooleanField(default=False, verbose_name="是否是外部链接")

    class Meta:
        db_table = "cms_nav"
        verbose_name = "导航栏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
