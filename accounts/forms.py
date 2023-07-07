from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("first_name", "last_name","phone_number","email","password",'username')

        
class UserForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('billing_address',)
