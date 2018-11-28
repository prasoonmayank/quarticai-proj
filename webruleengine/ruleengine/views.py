from django.shortcuts import render, get_object_or_404
from .models import Rule

# Create your views here.
def index(request):
	return render(request, 'ruleengine/index.html')

def add_rules(request):
	signal_id = request.POST["signalid"]
	vartype = request.POST["vartype"]
	varcondition = request.POST["varcondition"]

	print(signal_id, " ",vartype, " ",varcondition)

	given_rule = Rule(signal_id=signal_id,vartype=vartype,varcondition=varcondition)
	given_rule.save()
	return render(request, 'ruleengine/result.html')

