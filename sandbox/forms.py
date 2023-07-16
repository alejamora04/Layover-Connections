# Format Built-In Django Server-side validated forms here
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event

# Event model [Prototype]
# Formatting for event creation.
class EventCreationForm(forms.ModelForm):
	title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
	start_time = forms.CharField(label= 'Start Time: [ yyyy-mm-dd 00:00 ]')

	class Meta:
		model = Event
		fields = ['title', 'start_time', 'end_time']



"""

# Protype Custom Image forms Custom Django Image Upload Formatting
from django.forms.widgets import ClearableFileInput

# PROTOTYPE - Custom Django Imgae HTML Formatting
class CustomImageFieldWidget(ClearableFileInput):
	template_with_clear = 'layoverconnections/imageuploadform.html'

# PROTOTYPE - Custom Django Image Upload Form
class ImageUploadForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['userimage_1',]
		widgets = {
            'userimage_1': CustomImageFieldWidget,
		}


"""