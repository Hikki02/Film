# from transliterate import translit
from django.db import models
from apps.categories.models import Category


class Product(models.Model):
    RATE_CHOICE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    category = models.ManyToManyField(Category, through='ProductCategoryRelation', related_name='category_product')
    name = models.CharField(max_length=250)
    year_of_release = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=50)
    num_of_ep = models.CharField(max_length=125)
    producer = models.CharField(max_length=125)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICE)
    desc = models.TextField()
    teg = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.name}'


class ProductCategoryRelation(models.Model):
    user = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class VideoProduct(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='product_video')
    name = models.CharField(max_length=150)
    video = models.FileField(upload_to='product/video/%Y/%m/%d/')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_image')
    image = models.ImageField(upload_to='product/image/%Y/%m/%d/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name}'


class ShortEpisodDesc(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='short_epis_desc')
    name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return f'{self.name}'