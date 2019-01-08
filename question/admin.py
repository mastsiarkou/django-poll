from django.contrib import admin
from question.models import Voter, Question, Vote

@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'date_of_birth', 'email_adress')

	
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id','question_text')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
	list_display = ('voter' ,'question_text', 'choice', 'pub_date')
	
