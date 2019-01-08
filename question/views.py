from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import VoteForm
from . models import Voter, Question, Vote
import pygal 

class BasePage(TemplateView):
	template_name = "question/templates/base_page.html"

def form_view(request):
	#Create Question  instance usind question`s id in the admin database
	question = Question.objects.get(question_text__exact='What is your favorite musical album?')
	if request.method == 'POST':
		form = VoteForm(request.POST)
		if form.is_valid():
			#Create Vote model instance and fill with data from Form
			voter = Voter(
				first_name=form.cleaned_data['first_name'], 
				last_name=form.cleaned_data['last_name'],
				date_of_birth=form.cleaned_data['date_of_birth'],
				gender = form.cleaned_data['gender'],
				email_adress = form.cleaned_data['email_adress']
				)
			voter.save()
			"""Create Vote model instance using voter, and question_text as
			foreign key and fill with data from the Form"""
			vote = Vote(
				voter=voter, 
				question_text=question, 
				choice = form.cleaned_data['choices']
				)
			vote.save()
			return HttpResponseRedirect('/vote/results',{'question': question})
	else:
		form = VoteForm()

	return render(request, 'form_question.html', {'form': form, 'question': question})

def results(request):
	question = Question.objects.get(question_text__exact='What is your favorite musical album?')
	pie_chart = pygal.Pie()
	pie_chart.title = question.question_text
	radiohead_num = Vote.objects.filter(choice__exact='1').count()
	pink_floyd_num = Vote.objects.filter(choice__exact='2').count()
	the_beatles_num = Vote.objects.filter(choice__exact='3').count()
	massive_attack_num = Vote.objects.filter(choice__exact='4').count()
	nirvana_num = Vote.objects.filter(choice__exact='5').count()
	
	pie_chart.add('Kid A', radiohead_num)
	pie_chart.add('The wall ', pink_floyd_num)
	pie_chart.add('Abbey Road', the_beatles_num)
	pie_chart.add('Mezzanine', massive_attack_num)
	pie_chart.add('Nevermind', nirvana_num)
	image=pie_chart.render()
	#number_of_vote = all_votes.count() 

	return render(request, 'results.html', {'image':image})
