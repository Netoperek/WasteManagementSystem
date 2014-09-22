from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Address(models.Model):
	street = models.CharField(max_length=30, null=True, blank=False)
	number = models.IntegerField(null=True, blank=False)
	postCode = models.CharField(max_length=10, null=True, blank=False)
	city = models.CharField(max_length=30, null=True, blank=False)
