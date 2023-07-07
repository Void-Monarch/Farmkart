from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.urls import reverse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import redirect
from carts.models import CartItem
from store.views import store

# Create your views here.

def homepage_site(request,cart_cost=0,cart_items=0):
    cart_cost = 2000
    cart_items = 5
    
    if request.method == "POST":
        category_slug = request.POST['category_select']

        if category_slug == "all_categories":
            return redirect("store",)
        else:
            return store(request,category_slug=category_slug)
    
    product = Product.objects.all().filter(is_available=True)
    product = product[:8]
    context = {
        'total_items': len(CartItem.objects.all()),
        'products':product,
        }
    
    

    return render(request, 'homepage_site/homepage_site.html', context)




@xframe_options_exempt
def home_slider(request):
    a = {}
    return render(request, "homepage_site/home_slider.html", a )



