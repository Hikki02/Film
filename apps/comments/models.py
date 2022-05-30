from django.db import models


class ProductComment(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True,
                               related_name='children')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_comments')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product_comments')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LikeComment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE,
                             related_name='like_comments')
    comment = models.ForeignKey(ProductComment, on_delete=models.CASCADE,
                                related_name='likes_comment')
    like = models.BooleanField(default=False)

    class Meta:
        db_table = 'like_comment'


"""Добавить фото"""
