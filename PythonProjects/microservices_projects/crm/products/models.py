from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


class SubCategory(models.Model):
    sub_name = models.CharField(max_length=50)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
