from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from points.models import Point

class PointResource(ModelResource):
	#route = fields.ForeignKey(RouteResource, 'Route')

	class Meta:
		queryset = Point.objects.filter(Route = '2')
		resource_name = 'point'
		filtering = {"id" : ALL, "route" : ALL, "route__mobileUser" : ALL}

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']