# Format Built-In Django Server-side validated forms here
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
# PROTOTYPE - Custom Django Image Upload Formatting
from django.forms.widgets import ClearableFileInput

# Create your forms here.
# User Registration forms
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# Allows you to change User name and email address
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email']

# Provides Front-End controls to modify the user model on the profile page
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'age', 'hometown']

"""
# Formatting for image upload forms
class ImageUploadForm(forms.ModelForm):
	image = forms.ImageField(label= 'Upload Image')

	class Meta:
		model = Profile
		fields = ['image', 'userimage_1', 'userimage_2', 'userimage_3', 'userimage_4']
"""

# Biography form modified from comment form
class AboutMeForm(forms.ModelForm):
	bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 7}))

	class Meta:
		model = Profile
		fields = ['bio']


# PROTOTYPE - Custom Image Upload  Form
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
# Custom Django Image Upload Formatting
from django.forms.widgets import ClearableFileInput
"""