# from transliterate import translit
from django.db import models

from .utils import get_upload_path, RATE_CHOICE


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProductUserRelation(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='rela_user')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='rela_product')

    is_bookmark = models.BooleanField(default=False, null=True, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICE, null=True, blank=True)

    class Meta:
        db_table = 'product_user_relation'


class Producer(BaseModel):
    name = models.CharField(max_length=70)

    class Meta:
        db_table = 'producer'

    def __str__(self):
        return f'{self.name}'


class Product(BaseModel):
    name = models.CharField(max_length=250)
    year_of_release = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=50)  # choice field
    num_of_ep = models.CharField(max_length=125)
    description = models.TextField()
    teg = models.CharField(max_length=225)  # need to create Many to many

    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    user = models.ManyToManyField('users.User', through='ProductUserRelation', related_name='user_product')
    category = models.ManyToManyField('categories.Category', related_name='product_categ')

    is_ongoing = models.BooleanField(default=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f'{self.name}'


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_image')
    image = models.ImageField(upload_to=get_upload_path)
    is_main = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_image'

    def __str__(self):
        return f'{self.product.name}'


class ProductVideo(BaseModel):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE,
                                related_name='product_video')
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to='product/video/%Y/%m/%d/')
    description = models.TextField(null=True, blank=True)  # short desc of epis

    class Meta:
        db_table = 'product_video'

    def __str__(self):
        return f'{self.name}'
