from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

from .models import News, NewsImages, Product, ProductImages, MainImage


class GalleryInline(admin.TabularInline):
    fk_name = 'post'
    model = NewsImages


class ProductGallery(admin.TabularInline):
    fk_name = 'product'
    model = ProductImages


class ProductAdmin(ImportExportModelAdmin):
    inlines = [ProductGallery, ]
    list_display = ['title', 'brand', 'capacity']
    list_display_links = ['title']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class MainImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'get_img']
    list_display_links = ['title']
    fields = ('title', 'status', 'image')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100px">')


admin.site.register(MainImage, MainImageAdmin)


class NewsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]
    list_display = ['title', 'description', 'date']
    list_display_links = ['title']
    fields = ('title', 'description', 'date', 'text')


admin.site.register(News, NewsAdmin)

