from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Property(models.Model):
    owner_name = models.CharField(max_length=30)
    landmark = models.CharField(max_length=80, default=None)
    address1 = models.TextField(max_length=100)
    address2 = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    rent = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    rentedby = models.CharField(max_length=200,null=True, blank=True)