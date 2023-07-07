from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_site, name="homepage_site"),
    path('123123/', views.home_slider, name="home_slider"),

]
