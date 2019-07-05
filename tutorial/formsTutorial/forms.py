from django import forms 
from .models import Author, Book , Patient
from django.forms import ModelForm


BIRTH_YEAR_CHOICES = list(range(1900,2019,1))

class NameForm(forms.Form):
	your_name = forms.CharField(label='Name', max_length = 10)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget= forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

class AuthorForm(ModelForm):
	birth_date = forms.DateField(widget=forms.SelectDateWidget(years = BIRTH_YEAR_CHOICES))
	class Meta:
		model = Author
		fields =['name','title','birth_date']

class BookForm(ModelForm):
	class Meta: 
		model = Book
		fields = ['name', 'authors']

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		widgets = {
		'chart_id':forms.TextInput(attrs={'class':"form-control" }),
		'name':forms.TextInput(attrs={'class':"form-control" }),
		'age':forms.TextInput(attrs={'class':"form-control" }),
		'phone':forms.TextInput(attrs={'class':"form-control" }),
		'address':forms.TextInput(attrs={'class':"form-control" }),
		'memo':forms.Textarea(attrs={'class':"form-control",\
									 'style':"border:dashed 2px grey",
									 'rows':'5',
									 'padding-left':'80px',
									 }),
		}
		fields = '__all__'