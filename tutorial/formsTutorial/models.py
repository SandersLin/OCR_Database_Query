from django.db import models

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length = 100)
	title = models.CharField(max_length =3, choices = TITLE_CHOICES)
	birth_date = models.DateField(blank=True, null = True)
	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	def __str__(self):
		return self.name

class Patient(models.Model):
	chart_id = models.CharField(max_length =10,  blank = False, unique=True)
	name = models.CharField(blank = False, max_length= 100) 
	age = models.IntegerField(blank =True, null =True)
	phone= models.CharField(blank = True, max_length=20 , null =True)
	address = models.CharField(blank =True, max_length=100, null =True)
	memo = models.TextField(blank =True, null =True)
	def __str__(self):
		return self.name
