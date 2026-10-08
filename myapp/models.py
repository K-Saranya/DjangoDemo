from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=250)
    student_email = models.EmailField(max_length=254)

class DressCategory(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    
class Dress(models.Model):
    dress_name = models.CharField(max_length=150)
    dress_price = models.CharField(max_length=50)
    dress_image = models.URLField(max_length=6000)
    dress_category = models.ForeignKey(DressCategory,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.dress_name