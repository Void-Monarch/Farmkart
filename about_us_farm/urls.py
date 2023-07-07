from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_us, name="aboutus"),
]
