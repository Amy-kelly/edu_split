from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from userapp.models import User


def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token,
        'username':user.username,
        'user_id':user.id
    }

def get_user_by_account(account):
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