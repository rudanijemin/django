from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    date=models.DateField()

    def _str_(self):
        return self.name

    
