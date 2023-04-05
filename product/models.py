from django.db import models
from account.models import CustomerUser


class Category(models.Model):

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

COUNTRY_CHOICE = (
    ('UZBEKISTAN', 'uzbekistan'),
    ('KYRGIZISTAN', 'kyrgizistan'),
    ('KAZAKHSTAN', 'kazakhstan'),
    ('TURKMENISTAN', 'turkmenistan'),
    ('TADJIKISTAN', 'tadjikistan'),
)
