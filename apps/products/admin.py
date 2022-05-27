from django.contrib import admin

from apps.products.models import Product, ProductCategoryRelation, VideoProduct, ProductImage, ShortEpisodDesc, \
    ProductUserRelation


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductCategoryRelation)
class ProductCategoryRelationAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductUserRelation)
class ProductUserRelationAdmin(admin.ModelAdmin):
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
