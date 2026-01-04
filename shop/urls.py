from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>', views.products_by_category, name='products_by_category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
