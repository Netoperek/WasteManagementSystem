from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from routes.models import Route
from tastypie.authorization import Authorization

class RouteResource(ModelResource):
	class Meta:
		queryset = Route.objects.all()
		resource_name = 'route'
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']
