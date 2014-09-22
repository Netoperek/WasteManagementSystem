from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from trackingPoints.models import TrackingPoint
from routes.api import RouteResource

class TrackingPointResource(ModelResource):
	route = fields.ForeignKey(RouteResource, 'route')

	class Meta:
		queryset = TrackingPoint.objects.all()
		resource_name = 'trackingPoint'
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']
