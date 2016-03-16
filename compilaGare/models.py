from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


SESSO_CHOICES = (
    ('M', 'M'),
    ('F', 'F'),
)
# Create your models here.
class Soggetto(models.Model):
    ruolo = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    indirizzo = models.CharField(max_length=50)
    citta = models.CharField(max_length=20)
    data_di_nascita = models.DateField(blank=True, null=True)
    sesso  = models.CharField(max_length=1, choices=SESSO_CHOICES)
    
    
class Gara(models.Model):
    campo_gara_prova = models.CharField(max_length=30)
    
class Azienda(models.Model):
    campo_azienda_prova = models.CharField(max_length=30)
