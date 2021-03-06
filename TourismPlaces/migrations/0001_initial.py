# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 18:04
from __future__ import unicode_literals

import TourismPlaces.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=TourismPlaces.models.image_upload_path, width_field='width_field')),
                ('height_field', models.IntegerField(default=450)),
                ('width_field', models.IntegerField(default=350)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Reviews_for_Tourism_places',
            },
        ),
        migrations.CreateModel(
            name='TourismPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('place_type', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_for', to='TourismPlaces.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=TourismPlaces.models.video_upload_path)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('tourism_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_of', to='TourismPlaces.TourismPlace')),
            ],
        ),
        migrations.AddField(
            model_name='tourismplace',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_for', to='TourismPlaces.Video'),
        ),
        migrations.AddField(
            model_name='review',
            name='tourism_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_of', to='TourismPlaces.TourismPlace'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='tourism_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_of', to='TourismPlaces.TourismPlace'),
        ),
    ]
