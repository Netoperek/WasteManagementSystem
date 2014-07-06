from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Address(models.Model):
	street = models.CharField(max_length=30, null=False, blank=False)
	number = models.IntegerField(null=False, blank=False)
	postCode = models.CharField(max_length=10, null=False, blank=False)
	city = models.CharField(max_length=30, null=False, blank=False)
