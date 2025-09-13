from django.db import models
from account.models import User

class Idea(models.Model):
    name = models.CharField(max_length=100)
    text= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default='....@gmail.com')
    
    def __str__(self):
        return self.name
    
class Custumer_Email(models.Model):
    email = models.EmailField(default='.....@gmail' , null=True)
    

class Reservations(models.Model):
    STATUS_CHOICE= [('pending','در انتظار تایید'),
                    ('confirmed','تایید شده'),
                    ('canceled',' لغو شده')]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    date = models.DateField()
    time = models.TextField()
    guest = models.PositiveIntegerField()
    note = models.TextField(default='...')
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')
    
    def __str__(self):
        return f"{self.name} -{self.date}-{self.time}"