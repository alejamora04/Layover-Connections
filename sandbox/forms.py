# Format Built-In Django Server-side validated forms here
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event

# Event model [Prototype]
# Formatting for event creation.
class EventCreationForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['title', 'start_time', 'end_time']



"""
# Unique Form Attributes
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 7}))
	image = forms.ImageField(label= 'Upload Image')
	
	class Meta:
		model = User
		fields = ['email', 'bio', 'image', 'userimage_1', 'userimage_2', 'userimage_3', 'userimage_4']


	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

		

"""



"""

# Protype Custom Image forms Custom Django Image Upload Formatting
from django.forms.widgets import ClearableFileInput

# Library Dependancy
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