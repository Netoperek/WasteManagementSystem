from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization 
from tastypie import fields
from address.models import Address

class AddressResource(ModelResource):	
	class Meta:
		queryset = Address.objects.all()
		resource_name = 'address'
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']
