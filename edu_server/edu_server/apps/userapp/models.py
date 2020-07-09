from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11,unique=True,verbose_name="手机号")
    user_img = models.ImageField(upload_to="user",blank=True,null=True,verbose_name="用户头像")
    class Meta:
        db_table = "cms_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    #
    # def __str__(self):
    #     return self.username
