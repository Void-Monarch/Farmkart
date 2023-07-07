from django.shortcuts import render
from .models import Categories

def menu(request):
    links = Categories.objects.all()
    return dict(links=links)
