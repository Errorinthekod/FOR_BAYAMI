from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from .models import User
from django.views.generic import CreateView,FormView
# Create your views here.

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'pages/sign_up.html'
    success_url = '/'

class SignInView(FormView):
    model = User
    form_class = SignUpForm
    template_name = 'pages/sign_in.html'
    success_url = '/'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username = username, email = email, password = password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('home')
            else:
                return HttpResponse('Пользователь забанен')
        else:
            return HttpResponse('Неверные данные или такого пользователя не существует')

def logout2(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')

class LoginView(FormView):
    model = User
    from_class = SignUpForm
    template_name = 'pages/sign_up.html'
    success_url = '/'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username = username, email = email, password = password)






