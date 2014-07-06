from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from points.models import Point
from routes.api import RouteResource
from address.api import AddressResource
from mobileUsersRoutes.models import MobileUserRoute
from mobileUsers.api import MobileUserResource

class MobileUsersRouteResource(ModelResource):
	mobileUser = fields.ForeignKey(MobileUserResource, 'mobileUser')
	route = fields.ForeignKey(RouteResource, 'route')

	class Meta:
		queryset = MobileUserRoute.objects.all()
		resource_name = 'mobileUserRoute'
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']