from django.db import models
from django.conf import settings
from .models import Product

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'product')
        db_table = 'user_wishlist'
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"