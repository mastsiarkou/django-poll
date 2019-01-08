from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.core.exceptions import ValidationError
import datetime

class VoteForm(forms.Form):
	LIST_OF_ALBUM = (
		('1', 'Radiohead: Kid A'),
		('2', 'Pink Floyd: The wall'),
		('3', 'The Beatles: Abbey Road'),
		('4', 'Massive Attack: Mezzanine'),
		('5', 'Nirvana: Nevermind'),
		)
	GENDER_STATUS = (
	('F', 'Female'),
	('M', 'Male'),
	    )	
	years = [1940+i for i in range(100)]
	choices = forms.CharField(widget=forms.Select(choices=LIST_OF_ALBUM))
	first_name = forms.CharField()
	last_name = forms.CharField()
	date_of_birth = forms.DateField(widget = forms.SelectDateWidget(years=years))
	gender = forms.CharField(widget=forms.Select(choices=GENDER_STATUS))
	email_adress = forms.EmailField(max_length=35)