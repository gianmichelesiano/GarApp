# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilaGare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soggetto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruolo', models.CharField(max_length=30)),
                ('cognome', models.CharField(max_length=30)),
                ('nome', models.CharField(max_length=30)),
                ('indirizzo', models.CharField(max_length=50)),
                ('citta', models.CharField(max_length=20)),
                ('data_di_nascita', models.DateField(blank=True, null=True)),
                ('sesso', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
            ],
        ),
    ]
