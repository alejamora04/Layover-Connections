from django import forms
from .models import Event

# Event model forms
# Formatting for event creation.
class EventCreationForm(forms.ModelForm):
	title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
	start_time = forms.CharField(label= 'Start Time: [ yyyy-mm-dd 00:00 ]')
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
	# TODO Fix the default event_thumbnail error.
	#event_thumbnail = forms.ImageField(required=False)
	event_thumbnail = forms.ImageField()

	class Meta:
		model = Event
		fields = ['title', 'event_thumbnail', 'start_time', 'end_time', 'description']


# [Placeholder form] in case I make the update form different.
class EventUpdateForm(forms.ModelForm):
	title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
	start_time = forms.CharField(label= 'Start Time: [ yyyy-mm-dd 00:00 ]')
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
	event_thumbnail = forms.ImageField()

	class Meta:
		model = Event
		fields = ['title', 'event_thumbnail', 'start_time', 'end_time', 'description']

