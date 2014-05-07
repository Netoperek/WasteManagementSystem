from django.db import models
from mobileUsers.models import MobileUser
from routes.models import Route
# Create your models here.

class MobileUserRoute(models.Model):
	mobileUser = models.ForeignKey(MobileUser, null=False, blank=False)
	route = models.ForeignKey(Route, null=False, blank=False)
	date = models.DateField(auto_now=True)
	