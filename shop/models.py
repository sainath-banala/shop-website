from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        # by default Django adds 's' at the end of class name, which will become "Categorys", which is not appropriate 
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    # Allows accessing all products via category.products.all() instead of default category.product_set.all()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') 
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, help_text="Image URL from web") # we shall change it later, for now we shall use URL's
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # - means descending order ['-created_at'] -> newest first, ['created_at'] -> oldest first
        ordering = ['-created_at']

    def __str__(self):
        return self.name