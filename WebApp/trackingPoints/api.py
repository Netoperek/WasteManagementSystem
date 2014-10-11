from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from trackingPoints.models import TrackingPoint
from trackingRoutes.api import TrackingRouteResource

class TrackingPointResource(ModelResource):
	trackingRoute = fields.ForeignKey(TrackingRouteResource, 'trackingRoute')

	class Meta:
		queryset = TrackingPoint.objects.all()
		resource_name = 'trackingPoint'
                authentication = BasicAuthentication()
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']
