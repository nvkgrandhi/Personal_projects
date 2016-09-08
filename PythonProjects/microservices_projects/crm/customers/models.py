from django.db import models

# Create your models here.


class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    c_address = models.TextField()
    shipping_address = models.TextField()
    billing_address = models.TextField()
    # date_entered = models.DateTimeField()
    c_username = models.CharField(max_length=50)
    c_password = models.CharField(max_length=50)
