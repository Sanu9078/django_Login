from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    PhoneNumber=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name