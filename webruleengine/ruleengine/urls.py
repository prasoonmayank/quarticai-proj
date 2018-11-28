from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('add_rules/', views.add_rules, name='add_rules')
]
