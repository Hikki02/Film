from django.contrib import admin

# Register your models here.
from apps.comments.models import ProductComment


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    ...
