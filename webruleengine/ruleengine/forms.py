from django import forms
from .models import Rule

class RulesForm(forms.Form):
	signal = forms.CharField()
	var_type = forms.CharField()
	condition = forms.CharField()

	class Meta:
		model = Rule
		fields = ('signal','var_type','condition')

