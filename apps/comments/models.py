from django.db import models


class ProductComment(models.Model):
    user = models.ManyToManyField(to=users)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True,
                               related_name='children')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""Добавить фото и лайки к коментам"""


