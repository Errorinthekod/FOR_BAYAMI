from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.views.generic import CreateView

from .forms import ContactForm, SearchForm
from ..post.forms import CommentForm
from ..post.models import *
from .models import About, Contact
from ..post.views import Post, Category
# Create your views here.



class HomePageView(TemplateView):
    model = Post
    template_name = 'pages/home.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posta'] = Post.objects.all()[:3]
        context['categories'] = Category.objects.all() # одно и тоже
        context['form'] = CommentForm()

        return context

    def get_queryset(self): #Поисковик
        search_text = self.request.GET.get('query')
        if search_text is None:
            return Post.objects.all()
        q = self.model.objects.filter(
            Q(title__icontains = search_text) | # and - |
            Q(text__icontains=search_text) |
            Q(text2__icontains=search_text) |
            Q(text3__icontains=search_text)
        )
        return q




class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'



class AboutPageView(TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all() # одно и тоже

        return context

class ContactView(CreateView):
    model = Contact
    class_form = ContactForm
    success_url = '/'
    template_name = 'pages/contact.html'



































