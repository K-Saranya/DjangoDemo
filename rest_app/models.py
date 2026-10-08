from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length=50)
    
class UserOtherInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=50)


    
    
    