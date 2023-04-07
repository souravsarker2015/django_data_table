from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    salary = models.IntegerField(null=True)
    occupation = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)

