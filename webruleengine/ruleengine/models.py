from django.db import models

# Create your models here.
class Rule(models.Model):
	INT = 'Integer'
	STR = 'String'
	DTM = 'Datetime'
	VAR_CHOICES = (
		(INT, 'Integer'),
		(STR, 'String'),
		(DTM, 'Datetime'),
		)
	rule_signal = models.CharField(max_length=10)
	rule_vartype = models.CharField(max_length=8)
	# rule_vartype = models.CharField(max_length=3, choices=VAR_CHOICES, default=INT)
	rule_condition = models.CharField(max_length=200)

	def __str__(self):
		return self.rule_condition
