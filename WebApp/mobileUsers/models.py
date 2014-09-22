from django.db import models
from django.utils.encoding import smart_unicode

class MobileUser(models.Model):
	login = models.CharField(max_length = 30, null=False, blank=False)
	password = models.CharField(max_length = 30, null=False, blank=False)

	def __unicode__(self):
		return smart_unicode(self.login)
