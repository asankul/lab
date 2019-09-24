from django.contrib import admin
from webapp.models import Products


class ProductsAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'category', 'count', 'price']
    list_filter = ['name', 'category', 'price']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'count', 'price']


admin.site.register(Products, ProductsAdmin)

