from django.db import models
from django.utils.encoding import smart_unicode

from mobileUsers.models import MobileUser

# Create your models here.
class Route(models.Model):
	mobileUser = models.ForeignKey(MobileUser, null=True, blank=True)
	doDate = models.DateField(auto_now=True)#CHANGE LATER

class Point(models.Model):
	Route = models.ForeignKey(Route,null=False, blank=False)
	Longitude = models.FloatField(null=False, blank=False)
	Latitude = models.FloatField(null=False, blank=False)
	Address = models.CharField(max_length = 100, null=False, blank=False)

	def __unicode__(self):
		return smart_unicode(self.Address)



