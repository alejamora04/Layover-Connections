from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings

# Creates a User Profile with a one to one relationship with User Model
# Contains information for: profilepic, hometown, age, bio
class Profile(models.Model):
    # Create a one to one relationship with the User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    hometown = models.CharField(max_length= 25, null=True)
    age = models.IntegerField(null=True)
    profile = models.CharField(max_length=500,
                                blank=True)
    bio = models.CharField(max_length=500,
                            blank=True)

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