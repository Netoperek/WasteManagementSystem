from django import forms

from .models import MobileUser

class MobileUserForm(forms.ModelForm):
	class Meta:
		model = MobileUser