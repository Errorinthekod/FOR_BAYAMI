from django import forms
from .models import *


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs = {'placeholder': 'Введите текст комментария', 'class': 'form-control'})
        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required = False)



