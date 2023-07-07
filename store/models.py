from django.db import models
from django.urls import reverse
from categories.models import Categories

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True,)
    price = models.IntegerField()
    image = models.ImageField(blank=True,upload_to="photo/products")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True,)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
