from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from formulars.models import Formular
from mobileUsers.api import MobileUserResource
from points.api import PointResource

class FormularResource(ModelResource):
	mobileUser = fields.ForeignKey(MobileUserResource, 'mobileUser')
	point = fields.ForeignKey(PointResource, 'point')

	class Meta:
		queryset = Formular.objects.all()
		resource_name = 'formular'
		#filtering = {"id" : ALL, "route" : ALL, "mobileUser" : ALL, "address" : ALL} 
		authorization = Authorization()

	def alter_list_data_to_serialize(self, request, data):
		return data['objects']