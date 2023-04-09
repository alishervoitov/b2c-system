from django.db import models

from account.models import CustomerUser

class Order(models.Model):

    STATUSES = [
        ('PENDING', 'pending'),
        ('INPROGRESS', 'inprogress'),
        ('COMPLATED', 'complated'),
        ('CANCELED', 'canceled')
    ]

    customer = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True, related_name='orders')
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField(null=True)
    required_date = models.DateTimeField(null=True)
    shipped_date = models.DateTimeField(null=True)
    canceled_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='PENDING')

    def __str__(self):
        return f'{self.customer.__str__()} -> order:{self.id}'