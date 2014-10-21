from django.contrib.auth.models import User
user = User.objects.create_user('admin', 'lennon@thebeatles.com', '123qwe')
from userroles.models import set_user_role
from userroles import roles
set_user_role(user,roles.admin)
