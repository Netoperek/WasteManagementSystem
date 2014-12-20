from django.contrib.auth.models import User
from webAppUser.models import WebAppUser
user = User.objects.create_user('admin', 'lennon@thebeatles.com', '123qwe')
from userroles.models import set_user_role
from userroles import roles
set_user_role(user,roles.admin)
web_app_user = WebAppUser(user = user)
web_app_user.save()
