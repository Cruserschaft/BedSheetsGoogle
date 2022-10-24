import os
import uuid
from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="Тег")
    order = models.PositiveSmallIntegerField(unique=True, verbose_name="Порядок")
    access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = "Тип Товару"
        ordering = ("access", "order")


class ProductExtra(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    cost = models.IntegerField(verbose_name="Вартість")
    access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return f"{self.cost} грн: {self.title}"

    class Meta:
        verbose_name_plural = verbose_name = "Додаткові опції"


class Product(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/products/', filename)

    title = models.CharField(max_length=100, db_index=True, verbose_name="Назва")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="Тег")
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name="Тип")
    about = models.TextField(blank=True, verbose_name="Опис")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    access = models.BooleanField(default=True, verbose_name="Доступ")
    favorite = models.BooleanField(default=False, verbose_name="Обране (на головну)")
    datetime_create = models.DateTimeField(auto_now=True, verbose_name="Дата і час створення/оновлення")
    extra1 = models.ForeignKey(ProductExtra, on_delete=models.PROTECT, verbose_name="Додатково 1", null=True,
                               related_name="+", blank=True)
    extra2 = models.ForeignKey(ProductExtra, on_delete=models.PROTECT, verbose_name="Додатково 2", null=True,
                               related_name="+", blank=True)
    extra3 = models.ForeignKey(ProductExtra, on_delete=models.PROTECT, verbose_name="Додатково 3", null=True,
                               related_name="+", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = "Товари"
        ordering = ("-datetime_create", )


class ProductSubtype(models.Model):
    parent = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Продукт")
    title = models.CharField(max_length=50, verbose_name="Назва")
    cost = models.IntegerField(verbose_name="Вартість")
    access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return f"{self.parent.title}: {self.title}"

    class Meta:
        verbose_name_plural = verbose_name = "Вид товару"


