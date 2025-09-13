from django.db import models
from menu.models import Food 
from account.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank =True)
    session_key = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        if self.user:
            return f"Cart of {self.user.username}"
        return f"Guest Cart {self.id}"
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0) 
                                                                                                                                                                                                                                                                                                                                                                                                                   
    class Meta :
        unique_together = ('cart', 'food')
        
    def __str__(self):
        return f"{self.food.name}  x {self.quantity}"
    
    @property
    def subtotal(self):
        return self.food.price * self.quantity