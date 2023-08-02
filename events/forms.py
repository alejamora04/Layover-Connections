# Format Built-In Django Server-side validated forms here
from django import forms
from .models import Event

# Event model [Prototype]
# Formatting for event creation.
class EventCreationForm(forms.ModelForm):
	title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
	start_time = forms.CharField(label= 'Start Time: [ yyyy-mm-dd 00:00 ]')

	class Meta:
		model = Event
		fields = ['title', 'start_time', 'end_time', 'description']
