from django.db import models

# Create your models here.


class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    # hire_date = models.DateField()
    # birth_date = models.DateField()


class Departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept = models.OneToOneField(Employees, on_delete=models.CASCADE)


