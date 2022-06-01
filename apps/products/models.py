# from transliterate import translit
from django.db import models
from .settings import RATE_CHOICE


class ProductUserRelation(models.Model):
    is_bookmark = models.BooleanField(default=False, null=True, blank=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='rela_user')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='rela_product')
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICE, null=True, blank=True)


class Product(models.Model):
    category = models.ManyToManyField('categories.Category', related_name='product_category')
    user = models.ManyToManyField('users.User', through='ProductUserRelation', related_name='user_product')
    name = models.CharField(max_length=250)
    year_of_release = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=50)
    num_of_ep = models.CharField(max_length=125)
    producer = models.CharField(max_length=125)
    desc = models.TextField()
    teg = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.name}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_image')
    image = models.ImageField(upload_to='product/image/%Y/%m/%d/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name}'


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE,
                                related_name='product_video')
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to='product/video/%Y/%m/%d/')
    desc = models.TextField(null=True, blank=True)  # short desc of epis

    def __str__(self):
        return f'{self.name}'
