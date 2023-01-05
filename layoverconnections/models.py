from django.db import models
from django.contrib.auth.models import User

# Import the pre-configured User Model
class Profile(models.Model):
    # Create a one to one relationship with the Users
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Create a Field to hold the user uploaded image
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'