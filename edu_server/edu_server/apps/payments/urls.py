from django.urls import path

from payments import views

urlpatterns = [
    path("ali_pay/",views.AliPayAPIView.as_view()),
    path("pay_result/",views.AliPayResultAPIView.as_view())
]