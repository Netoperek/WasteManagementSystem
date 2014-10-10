from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.constants import ALL
from tastypie import fields
from trackingRoutes.models import TrackingRoute
from tastypie.authorization import Authorization

class TrackingRouteResource(ModelResource):
	class Meta:
		queryset = TrackingRoute.objects.all()
		resource_name = 'trackingRoute'
                authentication = BasicAuthentication()
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']
