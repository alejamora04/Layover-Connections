from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings

# Import the pre-configured User Model
class Profile(models.Model):
    # Create a one to one relationship with the User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Create a Field to hold the user uploaded profile picture image.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # DOB populate user age new information
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        # Provide size restrictions of user uploaded images (300x300)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
