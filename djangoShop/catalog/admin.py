from django.contrib import admin
from .models import Product, Gallery

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


admin.site.register(Gallery)
# Register your models here.
