from tastypie.resources import ModelResource
from tastypie.constants import ALL
from routes.models import Point
from routes.models import Route

class PointResource(ModelResource):
	class Meta:
		queryset = Point.objects.all()
		resource_name = 'point'
		filtering = {"id" : ALL}

class RouteResource(ModelResource):
	class Meta:
		queryset = Route.objects.all()
		resource_name = 'route'
		filtering = {"id" : ALL}