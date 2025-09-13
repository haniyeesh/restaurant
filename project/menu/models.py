from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food')
    name= models.CharField(max_length=50)
    detail = models.TextField(max_length=100)
    image = models.ImageField(upload_to='menu/', blank=True , null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name