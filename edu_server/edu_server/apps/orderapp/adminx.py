#课程课时表
import xadmin

from orderapp.models import Order, OrderDetail


#订单表
class OrderModelAdmin(object):
    pass

xadmin.site.register(Order, OrderModelAdmin)

#订单详情表
class OrderDetailModelAdmin(object):
    pass

xadmin.site.register(OrderDetail, OrderDetailModelAdmin)