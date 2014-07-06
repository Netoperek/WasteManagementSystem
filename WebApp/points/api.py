from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authentication import BasicAuthentication
from tastypie import fields
from points.models import Point
from routes.api import RouteResource
from address.api import AddressResource

class PointResource(ModelResource):
	route = fields.ForeignKey(RouteResource, 'route')
	address = fields.ForeignKey(AddressResource, 'address')

	class Meta:

		queryset = Point.objects.all()
		queryset = Point.objects.filter(route = '67')
		print queryset
		resource_name = 'point'
		filtering = {"id" : ALL, "route" : ALL, "route__mobileUser" : ALL, "address" : ALL} 

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']