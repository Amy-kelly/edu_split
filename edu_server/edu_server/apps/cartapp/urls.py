from django.urls import path

from cartapp import views

urlpatterns = [
    path("cart/",views.CartViewSet.as_view({
        "post":"add_cart",
        "get":"cart_list",
        "patch":"change_select",
        "put":"change_expire",
        # "delete":"del_course"
    })),
    path("del_cart/<str:id>/",views.CartDeleteAPIView.as_view())
]