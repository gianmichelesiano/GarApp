# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilaGare', '0002_soggetto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Azienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_azienda_prova', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_gara_prova', models.CharField(max_length=30)),
            ],
        ),
    ]
