from django.forms import ModelForm
from . import models
from .models import RC
from django import forms


class RCForm(ModelForm):
	class Meta:
		model = RC
		fields = ('psdiscord', 'psmc', 'anps',)