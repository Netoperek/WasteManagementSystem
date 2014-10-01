from django.db import models
from mobileUsers.models import MobileUser
from trackingRoutes.models import TrackingRoute
from routes.models import Route

class MobileUserRoute(models.Model):
        mobileUser = models.ForeignKey(MobileUser, null=False, blank=False)
	route = models.ForeignKey(Route, null=True, blank=True)
	trackingRoute = models.ForeignKey(TrackingRoute, null=True, blank=True)
	date = models.DateField(auto_now=False)
