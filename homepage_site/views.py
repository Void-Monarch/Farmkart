from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage_site(request):
    cart_cost = 2000
    cart_items = 1
    return render(request, 'homepage_site/homepage_site.html',{'cart_cost':cart_cost, 'cart_items':cart_items})