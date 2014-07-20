from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from points.models import Point
from routes.api import RouteResource
from address.api import AddressResource
from mobileUsersRoutes.models import MobileUserRoute
from mobileUsers.api import MobileUserResource
from tastypie.exceptions import ImmediateHttpResponse
from django.http import HttpResponse


class MobileUsersRouteResource(ModelResource):
	mobileUser = fields.ForeignKey(MobileUserResource, 'mobileUser')
	route = fields.ForeignKey(RouteResource, 'route')

	class Meta:
		always_return_data = True
		queryset = MobileUserRoute.objects.all()
		resource_name = 'mobileUserRoute'
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']