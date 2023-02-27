from django.contrib import admin
from webapp.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'description', 'photo', 'count', 'price', 'created_at')
    list_filter = ('id', 'category', 'title', 'description', 'photo', 'count', 'price', 'created_at')
    search_fields = ('category', 'title', 'description', 'photo', 'price', 'count')
    fields = ('category', 'title', 'description', 'photo', 'count', 'price', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')


admin.site.register(Product, ProductAdmin)
