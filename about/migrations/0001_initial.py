# Generated by Django 4.1.2 on 2022-10-10 19:07

import about.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to=about.models.Feature.get_file_name, verbose_name='Зображення')),
                ('access', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Особливості',
                'verbose_name_plural': 'Особливості',
            },
        ),
        migrations.CreateModel(
            name='FeatureInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_left', models.CharField(max_length=500, verbose_name='Опис зліва <br>')),
                ('about_right', models.CharField(max_length=500, verbose_name='Опис справа <br>')),
            ],
            options={
                'verbose_name': 'Особливості Інфо',
                'verbose_name_plural': 'Особливості Інфо',
            },
        ),
    ]
