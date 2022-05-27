from django.contrib import admin

from apps.products.models import Product, ProductCategoryRelation, VideoProduct, ProductImage, ShortEpisodDesc


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductCategoryRelation)
class ProductCategoryRelationAdmin(admin.ModelAdmin):
    ...


@admin.register(VideoProduct)
class VideoProductAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    ...


@admin.register(ShortEpisodDesc)
class ShortEpisodDescAdmin(admin.ModelAdmin):
    ...
