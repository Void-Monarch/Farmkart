from django.db import models
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photo/categories', blank=True)
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def get_slug(self):
        return reverse('product_by_categories', args=[self.slug])

    def __str__(self) -> str:
        return self.category_name 
    

