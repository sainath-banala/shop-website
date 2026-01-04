from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'featured' ,'created_at']
    list_filter = ['category', 'available', 'featured']
    search_fields = ['name', 'description']
    list_editable = ['available', 'featured'] # Clickable checkboxes! [SAVE] button appears