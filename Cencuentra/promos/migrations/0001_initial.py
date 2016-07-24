# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('negocios', '0002_negocio_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='nombre')),
                ('article', models.URLField(verbose_name='articulo')),
                ('discountP', models.IntegerField(blank=True, verbose_name='descuento porcentaje')),
                ('discountC', models.IntegerField(blank=True, verbose_name='descuento cantidad')),
                ('negocio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='negocios.Negocio')),
            ],
            options={
                'verbose_name': 'Promo',
                'verbose_name_plural': 'Promos',
            },
        ),
    ]
