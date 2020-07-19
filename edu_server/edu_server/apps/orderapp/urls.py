from django.urls import path

from orderapp import views

urlpatterns = [
    path("pay_order/",views.OrderAPIView.as_view())
]