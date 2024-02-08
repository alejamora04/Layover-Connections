# Format Built-In Django Server-side validated forms here
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# User Registration forms
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2' ]

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# User Model information Related Forms
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email']
		  
class ProfileUpdateForm(forms.ModelForm):
	bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 7}))
	image = forms.ImageField()

	class Meta:
		model = Profile
		fields = ['image', 'age', 'hometown', 'bio']

# Formatting for image upload forms
class ImageUploadForm(forms.ModelForm):
	image = forms.ImageField(label= 'Upload Image')

	class Meta:
		model = Profile
		fields = ['image', 'userimage_1', 'userimage_2', 'userimage_3', 'userimage_4']
