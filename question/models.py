from django.db import models
from datetime import datetime 

class Voter(models.Model):
	GENDER_STATUS = (
		('F', 'Female'),
		('M', 'Male'),
	)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=1, choices=GENDER_STATUS, help_text='Your gender')
	email_adress = models.EmailField(max_length=35)
	
	class Meta:
		ordering = ['last_name', 'first_name', 'date_of_birth']
	
	def __str__(self):
		return f'{self.first_name}, {self.last_name}'

class Question(models.Model):
	question_text = models.TextField()
	
	def __str__(self):
		return f'{self.question_text[:50]}'

class Vote(models.Model):
	LIST_OF_ALBUM = (
		('1', 'Radiohead: Kid A'),
		('2', 'Pink Floyd: The wall'),
		('3', 'The Beatles: Abbey Road'),
		('4', 'Massive Attack: Mezzanine'),
		('5', 'Nirvana: Nevermind'),
		)
	voter = models.ForeignKey('Voter', on_delete=models.SET_NULL, null=True)
	question_text = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
	choice = models.CharField(max_length=1, choices=LIST_OF_ALBUM) 
	pub_date = models.DateTimeField(default=datetime.now, blank = True)
	
	class Meta:
		ordering = ['-pub_date']
	
	#def __str__(self):
		#return f'{self.question_text}, {self.voter.first_name}'
	
	
	
	
		
	
	