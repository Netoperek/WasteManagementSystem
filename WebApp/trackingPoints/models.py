from django.db import models
from routes.models import Route

class TrackingPoint(models.Model):
	route = models.ForeignKey(Route, null=True, blank=True)
	longitude = models.FloatField(null=False, blank=False)
	latitude = models.FloatField(null=False, blank=False)
