from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse , HttpResponseRedirect
from .forms import NameForm, ContactForm, AuthorForm, BookForm, PatientForm
from django.forms.models import model_to_dict
from .models import Patient

# Create your views here.

def get_name(request): 
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
	
			return  HttpResponseRedirect('/thanks/')
		
	else: 
		form = NameForm()

	return render(request,'formsTutorial/get_name.html',{
		'form':form, 
		})

def  thanks(request):
	return render(request, 'formsTutorial/thanks.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['coolsanderslin@gmail.com']
			if cc_myself:
				recipients.append(sender)
			send_mail(subject,message,sender,recipients)
			return HttpResponseRedirect('/thanks/')

	else:
		form = ContactForm()
	return render(request, 'formsTutorial/contact.html', {'form':form})

def authors(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save(commit= True)
			return HttpResponseRedirect('/thanks/')
	else:
		form =BookForm()
	return render(request, 'formsTutorial/authors.html', {'form':form})


def patients(request):
	msg= ""
	patients = None
	num_patient = 0
	if request.method == 'POST':
		form = PatientForm(request.POST)
		action = request.POST['action']
		if action == 'search':

			try: 
				filter_dict = {}
				if request.POST['chart_id'] != '' : filter_dict['chart_id__exact'] = request.POST['chart_id'] 
				if request.POST['name'] != '':  filter_dict['name__exact'] = request.POST['name'] 
				if request.POST['age'] != '' :  filter_dict['age__exact'] = request.POST['age']
				if request.POST['phone'] != '' : filter_dict['phone__exact'] = request.POST['phone'] 

				if len(filter_dict) == 0:
					raise Patient.DoesNotExist
					
				patient = Patient.objects.filter(**filter_dict)
				num_patient = patient.count()
				if patient.count() ==1:
					patient = patient[0]
				elif patient.count() > 1:
					patients = patient
					patient = patient[0]
					msg =  "there is more than one result"
				else: 
					raise Patient.DoesNotExist

				patient_dict = model_to_dict(patient)
				form = PatientForm(initial = patient_dict)
			except  Patient.DoesNotExist: 
				msg = 'patient does not exist. Please try again'
				
		elif action == 'create': 
			if form.is_valid():
				form.save(commit= True)
				return HttpResponseRedirect('/thanks/')
		elif action == 'clear': 
			form = PatientForm()


	else:
		form =PatientForm()
	return render(request, 'formsTutorial/patients.html', {'form':form, 
															'msg':msg,
															'patients':patients,
															'num_patient':num_patient, 
															})

def patient_detail(request, chart_id):

	patient = Patient.objects.get(chart_id__exact = chart_id)
	patient_dict = model_to_dict(patient)
	form = PatientForm(initial =patient_dict)
	return render(request, 'formsTutorial/patients.html', {'form':form})

def demo(request):
	return render(request, 'formsTutorial/demo.html')