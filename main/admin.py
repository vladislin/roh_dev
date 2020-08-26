from django.contrib import admin
from .models import News, NewsImages, Product, ProductImages, LoadImage, MainImage


class GalleryInline(admin.TabularInline):
    fk_name = 'post'
    model = NewsImages


class ProductGallery(admin.TabularInline):
    fk_name = 'product'
    model = ProductImages


@admin.register(News)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductGallery, ]


# admin.site.register(News)
# admin.site.register(NewsImages)
admin.site.register(MainImage)
admin.site.register(LoadImage)
