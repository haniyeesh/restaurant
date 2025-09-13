from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.hashers import make_password,check_password

class User(AbstractUser):
    ROLE_CHOICE = (
        ('customer', 'CUSTOMER'),
        ('manager', 'Restaurant Manager'),
        ('delivery', 'Delivery Person')
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default='customer')
    
    def __str__(self):
        return f"{self.role}-{self.username}"
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile', default=1)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    address = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', default='img/profile.jpg')
    
    def __str__(self):
        return f"profile {self.user.username}-{self.user.role}"


class Manager_permission(models.Model):
    permission = models.CharField(max_length=100)

    def __str__(self):
        return f"profile {self.permission}"