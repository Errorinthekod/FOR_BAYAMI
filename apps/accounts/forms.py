from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email',
               'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password',
               'class':'form-control'}))

class SignInForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email',
               'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password',
               'class':'form-control'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
        attrs = {'placeholder': 'Username',
                 'class': 'form-control'}))

    email = forms.CharField(widget = forms.TextInput(
        attrs = {'placeholder': 'Email',
                 'class': 'form-control'}))

    password = forms.CharField(widget = forms.TextInput(
        attrs = {'placeholder': 'Password',
                 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

