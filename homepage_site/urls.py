from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_site, name="homepage_site"),
]
