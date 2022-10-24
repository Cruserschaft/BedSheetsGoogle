import os
import uuid
from django.db import models


class FeatureInfo(models.Model):
    about_left = models.TextField(verbose_name='Опис зліва <br>')
    about_right = models.TextField(verbose_name='Опис справа <br>')

    class Meta:
        verbose_name = verbose_name_plural = 'Особливості Інфо'


class Feature(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/about/feature/', filename)
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    image = models.ImageField(upload_to=get_file_name, verbose_name='Зображення')
    access = models.BooleanField(default=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Особливості'


class Title(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/about/title/', filename)
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    about = models.TextField(verbose_name="Опис")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "Заголовок"

