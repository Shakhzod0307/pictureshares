from django.contrib import admin
from .models import Picture,Category

# Register your models here.


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['category','picture']
    search_fields = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# admin.site.register(Video)
