from django.db import models
from routes.models import Route
from address.models import Address

class Point(models.Model):
	route = models.ForeignKey(Route, null=True, blank=True)
	address = models.ForeignKey(Address, null=True, blank=True)
	longitude = models.FloatField(null=False, blank=False)
	latitude = models.FloatField(null=False, blank=False)
