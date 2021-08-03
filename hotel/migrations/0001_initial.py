# Generated by Django 3.2 on 2021-08-03 14:10

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_page', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('direction', models.CharField(max_length=255)),
                ('score_review', models.CharField(max_length=255)),
                ('score', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('photos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=5)),
            ],
            options={
                'db_table': 'scraper_hotel',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('room_code', models.CharField(max_length=15, unique=True)),
                ('size', models.CharField(blank=True, max_length=15, null=True)),
                ('photos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=5)),
                ('facilities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='hotel.hotel')),
            ],
            options={
                'db_table': 'scraper_room',
            },
        ),
        migrations.CreateModel(
            name='ReviewHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=100)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=2), size=100)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='hotel.hotel')),
            ],
            options={
                'db_table': 'scraper_review',
            },
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=255)),
                ('country_img', models.CharField(max_length=255)),
                ('positive_message', models.CharField(max_length=1000)),
                ('negative_message', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentary', to='hotel.reviewhotel')),
            ],
            options={
                'db_table': 'scraper_commentary',
            },
        ),
    ]