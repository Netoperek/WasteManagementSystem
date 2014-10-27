from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from points.models import Point
from trackingRoutes.api import TrackingRouteResource
from address.api import AddressResource
from routes.api import RouteResource
from mobileUsersRoutes.models import MobileUserRoute
from mobileUsers.api import MobileUserResource
from tastypie.exceptions import ImmediateHttpResponse
from django.http import HttpResponse
from tastypie.authorization import DjangoAuthorization


class MobileUsersRouteResource(ModelResource):
	mobileUser = fields.ForeignKey(MobileUserResource, 'mobileUser')
	trackingRoute = fields.ForeignKey(TrackingRouteResource, 'trackingRoute', null=True)
	route = fields.ForeignKey(RouteResource, 'route')

	class Meta:
		always_return_data = True
		queryset = MobileUserRoute.objects.all()
		resource_name = 'mobileUserRoute'
		filtering = {"id" : ALL, "date" : ALL, "mobileUser" : ALL} 
		authentication = BasicAuthentication()
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']
