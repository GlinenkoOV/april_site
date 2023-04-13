from django.contrib import admin
from .models import Product,Popular,Featured,Bloog, Brand, Unlimited, Home
# Register your models here.

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible','is_sale']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible', 'is_sale']

@admin.register(Popular)
class PopularAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible']

@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible']

@admin.register(Bloog)
class BloogAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Unlimited)
class UnlimitedAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['image']