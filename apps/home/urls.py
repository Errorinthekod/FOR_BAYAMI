from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('contact/', ContactPageView.as_view(), name = 'contact' ),
    path("about_us/", AboutPageView.as_view(), name = 'about_us')

]