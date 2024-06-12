# Generated by Django 5.0.6 on 2024-06-10 10:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('science', 'Science'), ('history', 'History'), ('politics', 'Politics')], max_length=100)),
                ('priority', models.IntegerField(default=2)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('keywords', models.CharField(blank=True, max_length=255)),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('sub_heading', models.CharField(blank=True, max_length=255)),
                ('sub_heading_2', models.CharField(blank=True, max_length=255)),
                ('context_1', models.TextField(blank=True)),
                ('context_2', models.TextField(blank=True)),
                ('context_3', models.TextField(blank=True)),
                ('context_4', models.TextField(blank=True)),
                ('context_5', models.TextField(blank=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'ordering': ['priority', '-date_added'],
            },
        ),
    ]
