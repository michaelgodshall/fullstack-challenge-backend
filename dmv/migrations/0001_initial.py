# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 03:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('zip', localflavor.us.models.USZipCodeField(max_length=10)),
                ('number_of_bedrooms', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('f', 'Female'), ('m', 'Male')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='dmv.Household')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('license_plate', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='dmv.Household')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='dmv.Person')),
            ],
        ),
    ]