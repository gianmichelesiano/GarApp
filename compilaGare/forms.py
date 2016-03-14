from django import forms
from .models import Post, Soggetto

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'created_date', 'text',)



class SoggetoForm(forms.ModelForm):
    class Meta:
        model = Soggetto
        fields = ('ruolo', 'cognome', 'nome','indirizzo','citta','data_di_nascita','sesso',)

