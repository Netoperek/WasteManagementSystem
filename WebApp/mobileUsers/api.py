from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from mobileUsers.models import MobileUser
from tastypie.authorization import Authorization

class MobileUserResource(ModelResource):
	class Meta:
		queryset = MobileUser.objects.all()
		resource_name = 'mobileUser'
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']
