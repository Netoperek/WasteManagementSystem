from django.db import models
from trackingRoutes.models import TrackingRoute

class TrackingPoint(models.Model):
	trackingRoute = models.ForeignKey(TrackingRoute, null=True, blank=True)
	longitude = models.FloatField(null=False, blank=False)
	latitude = models.FloatField(null=False, blank=False)
