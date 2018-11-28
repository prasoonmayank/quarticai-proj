from django.shortcuts import render, get_object_or_404
from .models import Rule
from .compute import 

# Create your views here.
def index(request):
	return render(request, 'ruleengine/index.html')

def add_rules(request):
	signal_id = request.POST.getlist('signalid')
	vartype = request.POST.getlist('vartype')
	varcondition = request.POST.getlist('varcondition')

	rules_json = convertIntoRules(signal_id, vartype, varcondition)

	return render(request, 'ruleengine/result.html')

