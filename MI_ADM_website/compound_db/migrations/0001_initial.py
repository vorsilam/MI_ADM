# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=13, unique=True)),
                ('description', models.TextField(blank=True)),
                ('smiles', models.CharField(max_length=2048)),
                ('inchi', models.CharField(max_length=2048)),
                ('inchi_key', models.CharField(max_length=27)),
                ('mol_weight_exact', models.FloatField()),
                ('heavy_atoms_count', models.IntegerField()),
                ('ring_count', models.IntegerField()),
            ],
        ),
    ]
