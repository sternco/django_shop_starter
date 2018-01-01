from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.a
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    product_des = models.CharField(max_length=400)
    product_price = models.CharField(max_length=10)
    product_image = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name
    