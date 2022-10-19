from unittest.util import _MAX_LENGTH
from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=10)

    def __str__(self):
        return self.order_number

class OrderDetail(models.Model):
    ORDER_CHOICES = [
        ('SHIPPED','SHIPPED'),
        ('PENDING','PENDING'),
        ('CANCELLED','CANCELLED')
    ]    

    order_number = models.ForeignKey(Order, on_delete=models.CASCADE,
                                        related_name='order_details')
    item_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=ORDER_CHOICES)

    def __str__(self):
        return f'{self.order_number} - {self.item_name} - {self.status}'
