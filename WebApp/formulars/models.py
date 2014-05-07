from django.db import models
from mobileUsers.models import MobileUser
from points.models import Point
# Create your models here.

class Formular(models.Model):
	mobileUser = models.ForeignKey(MobileUser, null=False, blank=False)
	point = models.ForeignKey(Point, null=False, blank=False)
	date = models.DateField(auto_now=False)
