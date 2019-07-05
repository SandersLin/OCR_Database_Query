from django.urls import path 

from . import views


urlpatterns = [
	path('get_name/', views.get_name, name= 'get name'),
	path('thanks/', views.thanks, name= 'thanks'), 
	path('contact/', views.contact, name = 'contanct'), 
	path('authors/', views.authors, name='authors'),
	path('patient/<str:chart_id>/', views.patient_detail, name='patient_detail'),
	path('patients/',views.patients, name='patients'),
	path('demo/', views.demo, name = 'demo'), 

]