from django.contrib.auth.models import User
class EmailAuthBackend:

    """
    Аутентифицировать посредством адреса электронной почты.
    """

    def authenticate(self, request, username=None, password=None):
         try:
             # users=User.objects.all()
             # for user in users:
             #    print(user.email, user.username)
             user = User.objects.get(email=username)
             if user.check_password(password):
                return user
             return None
         except (User.DoesNotExist, User.MultipleObjectsReturned):
             return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

from account.models import Profile

def create_profile(backend, user, *args, **kwargs):

    Profile.objects.get_or_create(user=user)