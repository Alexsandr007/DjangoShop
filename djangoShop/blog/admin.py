from django.contrib import admin
from .models import Category, Blog, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )