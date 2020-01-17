from django.db import models

from django.db import models


# Create your models here.
# model for products contains information about the name of each paper, its description, 
#its price and an image for each paper.

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    # allows user to see product displayed on screen.

    def __str__(self):
        return self.name
