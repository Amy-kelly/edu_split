from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from userapp.models import User


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'user_id': user.id
    }



#多方式验证的方法
def get_user_by_account(account):
    '''
           Q对象包括 AND 关系 和 OR 关系
           Q 对象可以用 & 和 | 运算符进行连接。当某个操作连接两个 Q 对象时，就会产生一个新的等价的 Q 对象
           -过滤器函数可以传递一个或多个Q对象作为位置参数，如果有多个Q对象，这些参数的逻辑为and
           过滤器函数可以混合使用Q对象和关键字参数，所有参数都将and在一起，Q对象必须位于关键字参数的前面
           '''
    try:
        user = User.objects.filter(Q(username=account) | Q(phone=account)).first()
    except User.DoesNotExist:
        return None
    else:
        return user


class UserAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        print(user)
        print(username)
        if user and user.check_password(password) and user.is_authenticated:
            return user
        else:
            return None



