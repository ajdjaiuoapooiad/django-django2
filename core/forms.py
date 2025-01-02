

from django import forms
from django.contrib.auth.models import User
from core.models import Post
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['user','text']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    class Meta:
        model= User