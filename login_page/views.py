from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required



# Create your views here.
def login_user_page(request):
    return render(request,'login/login_page.html', {})

def User_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username, password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('homepage')
            else:
                return HttpResponseRedirect('login')