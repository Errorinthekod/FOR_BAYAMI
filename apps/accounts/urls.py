from django.contrib.auth import logout
from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name = 'sign_up'),
    path('sign_in/', SignUpView.as_view(), name = 'sign_in'),
    path('logout/', logout2, name = 'logout')














]






