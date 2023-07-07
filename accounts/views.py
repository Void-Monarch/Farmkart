from django.shortcuts import render, redirect
from .models import Account
from django.contrib import auth
from .forms import RegistrationForm, UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlencode, urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        username = request.POST["username"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('homepage_site')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")

    return render(request, "loginandregister/login_page.html",)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,email=email,password=password,username = username,phone_number=phone_number )
            user.save()

            # current_site = get_current_site(request)
            # mail_subject = 'Please activate your account'
            # message = render_to_string('loginandregister/account_verification_email.html', {
            #     'user': user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token' : default_token_generator.make_token(user),
            # })

            # to_email = email
            # send_email = EmailMessage(mail_subject, message, to=[to_email])
            # send_email.send()

            return redirect('register')       
    else:
        form = RegistrationForm()
    context={
        'form': form,
    }
    return render(request, "loginandregister/register_page.html",context=context)

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("login")

def activate(request):
    return

@login_required(login_url='login')
def dashboard(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
    context={
        'user_form': user_form,    
    }
    return render(request, "loginandregister/dashboard.html",context=context)


