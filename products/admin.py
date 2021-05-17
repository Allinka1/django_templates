from django.contrib import admin
from products.models import Products, Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category']
    ordering = ['cid']
    list_display = ['category', 'cid']


admin.site.register(Category, CategoryAdmin)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ['category', 'brand', 'model']
    ordering = ['pid']
    list_display = ['category', 'pid', 'brand', 'model']
