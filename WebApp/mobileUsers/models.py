from django.db import models
from django.contrib.auth.models import User

class MobileUser(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30, null=False, blank=False)

    def __unicode__(self):
        return self.user.username
