from tastypie.resources import ModelResource
from tastypie.constants import ALL
from routes.models import Point
from routes.models import Route

class RouteResource(ModelResource):
	class Meta:
		queryset = Route.objects.all()
		resource_name = 'route'
		filtering = {"id" : ALL}

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']

class PointResource(ModelResource):
	#route = fields.ForeignKey(RouteResource, full=True)

	class Meta:
		queryset = Point.objects.all()
		resource_name = 'point'
		filtering = {"id" : ALL}

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']