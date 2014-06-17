from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from address.models import Address

class AddressResource(ModelResource):	

	class Meta:
		queryset = Address.objects.all()
		resource_name = 'address'
		filtering = {"id" : ALL}

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']