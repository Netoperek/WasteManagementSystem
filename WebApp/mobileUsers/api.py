from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from mobileUsers.models import MobileUser
from tastypie.exceptions import ImmediateHttpResponse
from django.http import HttpResponse
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

class MobileUserResource(ModelResource):
	class Meta:
		queryset = MobileUser.objects.all()
		resource_name = 'mobileUser'
		filtering = {"id" : ALL, "login" : ALL} 
		authorization = Authorization()
		authentication = BasicAuthentication()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']
