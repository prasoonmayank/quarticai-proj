from django.shortcuts import render, get_object_or_404
from .models import Rule
from django.http import HttpResponse
from .compute import convertIntoRules, get_string_result

# Create your views here.
def index(request):
	return render(request, 'ruleengine/index.html')

def add_rules(request):
	signal_id = request.POST.getlist('signalid')
	vartype = request.POST.getlist('vartype')
	varcondition = request.POST.getlist('varcondition')

	rules_json = convertIntoRules(signal_id, vartype, varcondition)

	ansstring = get_string_result(rules_json)
	print(ansstring)
	if(ansstring == ""):
		return HttpResponse("No signal with false rules")
	else:
		return HttpResponse(ansstring)

