from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
	context = {}
	return render(request, 'ruleengine/index.html', context)


