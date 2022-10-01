from django.urls import path
from homepage import views

urlpatterns = [
    path("", views.home, name="home"),
    path("homepage/name", views.hello_there, name="hello_there"),
]