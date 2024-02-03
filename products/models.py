from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    

class Brand(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    

class Product(models.Model):
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name