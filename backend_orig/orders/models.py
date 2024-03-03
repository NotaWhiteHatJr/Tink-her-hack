from django.db import models
from product.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )    
    o_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    o_qty = models.PositiveIntegerField(default=1)
    unit_price=models.DecimalField(max_digits=20,decimal_places=2)
    total_price=models.DecimalField(max_digits=20,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    #user -> f.k
    def __str__(self):
        o = str(self.o_id)
        return o
    

