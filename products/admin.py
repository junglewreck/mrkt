from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "description", "price"]
    search_fields = ["description", 'title']
    list_filter = ['price']
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
