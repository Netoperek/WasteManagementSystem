from django.db import models
from mobileUsers.models import MobileUser
from trackingRoutes.models import TrackingRoute

class MobileUserRoute(models.Model):
        mobileUser = models.ForeignKey(MobileUser, null=False, blank=False)
	trackingRoute = models.ForeignKey(TrackingRoute, null=False, blank=False)
	date = models.DateField(auto_now=True)
