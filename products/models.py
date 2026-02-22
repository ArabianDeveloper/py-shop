from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)
    # image = models.ImageField(upload_to = 'images/products/',blank=True, null=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    code = models.CharField(max_length=10)
    discription = models.CharField(max_length=255)
    discount = models.FloatField()
    def __str__(self):
        return self.code