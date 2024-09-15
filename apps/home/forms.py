from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your phone'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your subject'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your message'})
        }

        name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'name',
                   'class': 'form-control'}))

        email = forms.CharField(widget=forms.EmailInput(
            attrs={'placeholder': 'Email',
                   'class': 'form-control'}))


        phone = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'name',
                   'class': 'form-control'}))

        subject = forms.CharField(widget=forms.EmailInput(
            attrs={'placeholder': 'Email',
                   'class': 'form-control'}))

        message = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'name',
                   'class': 'form-control'}))

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required = False)
