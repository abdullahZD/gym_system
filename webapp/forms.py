from django import forms 
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm 
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput
from .models import Record
#register user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


#login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput)



#Record form
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','phone','category','tall','weight','address']

#Update form
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','phone','category','tall','weight','address']