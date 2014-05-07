from django.db import models
from mobileUsers.models import MobileUser
from points.models import Point
# Create your models here.

class Report(models.Model):
	mobileUser = models.ForeignKey(MobileUser, null=False, blank=False)
	point = models.ForeignKey(Point, null=False, blank=False)
	date = models.DateField(auto_now=False)
	#photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	