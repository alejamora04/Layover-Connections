from django.test import TestCase, Client
from .models import Profile
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Unit Test for Layover Connections app.

# Model Testing:
# [Profile] Unit test for model object.
class TestProfileModel(TestCase):

    # Setup dummy user to link ot a Profile.
    def setUp(self):
        # Create dummy user object to link to a Profile [one-to-one]
        self.user = User.objects.create_user(first_name = "John",\
                                             last_name = "Doe",\
                                             username = "John_Doe",\
                                             email = "johndoe@gmail.com",\
                                             password = "GenericPassword1234")

    # Remove Profile object once finished.
    def tearDown(self):
        pass

    # Creates Profile object ensures that it's created correctly and links it to user one-to-one.
    def test_profile_creation(self):
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(profile.user, self.user)

        # Test string output for queried model SQL Shell object.
        self.assertEqual(str(profile), f'{self.user.username} Profile')

    # Validate that image is sucessfully resized on save
    def test_image_resizing(self):
        # Create a profile for the user
        profile = Profile.objects.create(user=self.user)

        # Open the default image and check if it's resized
        img_path = profile.image.path
        img = Image.open(img_path)

        # Check if the image is resized to (300, 300)
        self.assertTrue(img.width <= 300)
        self.assertTrue(img.height <= 300)

    # Test custom model save method and ensures that it succesfully saves the image.
    def test_save_method(self):
        # Create a profile for the user
        profile = Profile.objects.create(user=self.user)

        # Open the default image and check if it's saved
        img_path = profile.image.path
        with open(img_path, 'rb') as img_file:
            self.assertIsNotNone(img_file.read())

    # Test whether Profile properly operates whent there are blank fields present.
    def test_blank_fields(self):
        profile = Profile.objects.create(user=self.user, hometown='', age=None, profile='', bio='')

        # Check if blank fields are saved
        self.assertEqual(profile.hometown, '')
        self.assertIsNone(profile.age)
        self.assertEqual(profile.profile, '')
        self.assertEqual(profile.bio, '')


# Views Testing:
# [Registration] Unit test for login & registration based views.
class TestViews(TestCase):

    # Setup dummy user to link ot a Profile.
    def setUp(self):
        # Create dummy user object to link to a Profile [one-to-one]
        self.user = User.objects.create_user(first_name = "John",\
                                             last_name = "Doe",\
                                             username = "John_Doe",\
                                             email = "johndoe@gmail.com",\
                                             password = "GenericPassword1234")

    # Remove Profile object once finished.
    def tearDown(self):
        pass

    # Test User login View.
    # Evaluate 200 HTTP status code for user log in. 
    def test_login_http_status_code(self):
        dummy_user = Client()
        login_url = reverse("layoverconnections:login")
        login_response = dummy_user.post(login_url, {"username": self.user.username, "password": self.user.password}, follow=True)
        login_status_code = login_response.status_code

        # Validate login functionality by checking for a 200 HTTP Status code.
        self.assertEqual(login_status_code, 200)
    

    # Validate functional login redirects.
    def test_login_redirect(self):
        dummy_user = Client()
        login_url = reverse("layoverconnections:login")
        login_response = dummy_user.post(login_url, {"username": self.user.username, "password": "GenericPassword1234"}, follow=True)

        # Check for successful login and redirect
        self.assertRedirects(login_response, reverse("layoverconnections:homepage"))
        # Check if the user is actually logged in
        self.assertTrue(login_response.wsgi_request.user.is_authenticated)

