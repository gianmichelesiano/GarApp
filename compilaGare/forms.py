from django import forms
from .models import Post, Soggetto, Gara, Azienda

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'created_date', 'text',)



class SoggetoForm(forms.ModelForm):
    class Meta:
        model = Soggetto
        fields = ('ruolo', 'cognome', 'nome','indirizzo','citta','data_di_nascita','sesso',)


class GaraForm(forms.ModelForm):
    class Meta:
        model = Gara
        fields = ('campo_gara_prova',)
        
class AziendaForm(forms.ModelForm):
    class Meta:
        model = Azienda
        fields = ('campo_azienda_prova',)

