from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from userapp import views

urlpatterns = [
    path("login/",obtain_jwt_token),
    path("captcha/",views.CaptchaAPIView.as_view()),
    path("register/", views.UserAPIView.as_view()),
    path("mobile/<str:mobile>/", views.MobileCheckAPIView.as_view()),
    path("sms/<str:mobile>/", views.SendMessageAPIView.as_view()),
    path("phone_login/",views.UserLoginViewSet.as_view({"post":"login"}))
]