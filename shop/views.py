from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.
def home(request):
    "HomePage with featured products"
    featured_products = Product.objects.filter(featured=True, available=True)
    categories = Category.objects.all()
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }

    return render(request, 'shop/home.html', context)

def product_list(request):
    "All Products page"
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, pk):
    "Single product detail page"
    product = get_object_or_404(Product, pk=pk, available=True)
    related_products = Product.objects.filter(
        category = product.category,
        available = True
    ).exclude(pk=pk)[:4]
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'shop/product_detail.html', context)

def products_by_category(request, category_id):
    "products filtered by category"
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category, available=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'current_category': category
    }
    return render(request, 'shop/product_list.html', context)

def about(request):
    "About us page"
    return render(request, 'shop/about.html')

def contact(request):
    "Context page"
    return render(request, 'shop/contact.html')