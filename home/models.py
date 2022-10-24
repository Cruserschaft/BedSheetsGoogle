import os
import uuid
from django.db import models


class Banner(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/home/banner/', filename)

    title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок')
    about = models.CharField(max_length=200, verbose_name='Опис')
    image = models.ImageField(upload_to=get_file_name, verbose_name='Зображення')
    button = models.CharField(max_length=50, verbose_name="Текст, кнопка", default="")
    access = models.BooleanField(default=True, verbose_name='Доступ')
    date_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = 'Реклама'
        ordering = ('date_create', 'title')


class Title_main(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/home/main/', filename)
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    about = models.TextField(verbose_name="Опис")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    button_title = models.CharField(max_length=20, verbose_name="Кнопка назва")
    access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "Заголовок"



