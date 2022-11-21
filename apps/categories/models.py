from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.PROTECT,
                               related_name='children', blank=True, null=True)
    name = models.CharField(max_length=255)

    is_main = models.BooleanField(default=False)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f'{self.name}'
