from django.db import models

class Order(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits = 7, decimal_places = 2)