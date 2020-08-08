from django import forms
from django.forms import ModelForm

from .models import Project

class PostForm(ModelForm):

	class Meta:
		model = Project
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}