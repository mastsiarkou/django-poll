from django.urls import path
from . import views

urlpatterns = [
	path('', views.BasePage.as_view(), name = 'base'),
	path('question', views.form_view, name = 'question'),
	path('results', views.results, name = 'results'),
]
