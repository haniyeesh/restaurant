from django.db import models
from account.models import User
from menu.models import Food

class Cart (models.Model):
    user = models.ForeignKey(User, null = True, blank= True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, null = True, blank= True, )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def total_quantity(self):
        return self.items.aggregate(total=models.Sum('quantity'))['total'] or 0

    def __str__(self):
        if self.user:
            return f"{self.user} cart"
        else:
            return f" gust cart"
   
        
class Cart_item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Food, on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=0)
    price_at_added = models.DecimalField(max_digits=10, decimal_places=3)
    discount = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    
    def get_total_price(self):
        return self.quantity *self.product.price