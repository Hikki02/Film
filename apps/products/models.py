from django.db import models
from apps.categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=225)
    year_of_release = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=225)  # Или будет manytomay with category
    type = models.CharField(max_length=50)
    num_of_ep = models.CharField(max_length=125)
    producer = models.CharField(max_length=125)
    rating = models.CharField(max_length=1)  # сделать выборочно
    desc = models.TextField()
    category = models.ManyToManyField(to=Category)  # сделай свою собственную связь с категори
    teg = models.CharField(max_length=225)


class VideoProduct(models.Model):
    name = models.CharField(max_length=150)
    video = models.FileField()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_image')
    image = models.ImageField(upload_to='product/uploads/%Y/%m/%d/')


class ShortEpisodDesc(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
