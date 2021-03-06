from django.contrib import admin

from apps.products.models import Product, ProductVideo, ProductImage, \
    ProductUserRelation


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductUserRelation)
class ProductUserRelationAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductVideo)
class VideoProductAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    ...
