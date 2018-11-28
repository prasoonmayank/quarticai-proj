from django import forms
from .models import Rule

class RulesForm(forms.Form):
	signal = forms.CharField(label='signal-Id')
	var_type = forms.ChoiceField(choices=[('Integer', 'Integer'), ('String', 'String'), ('Datetime', 'Datetime')])
	condition = forms.CharField()

	class Meta:
		model = Rule
		fields = ('signal','var_type','condition')

