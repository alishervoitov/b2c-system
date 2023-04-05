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

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    medicine_form = models.CharField(max_length=255)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICE)
    company = models.CharField(max_length=255)
    trade_name_of_the_drug = models.CharField(max_length=50)
    active_ingredient = models.CharField(max_length=255, null=True, blank=True)
    composition = models.TextField(max_length=1000)
    pharmacotherapeutic_group = models.TextField(max_length=5000)
    contraindication = models.TextField(max_length=5000)
    pharmacokinetic = models.TextField(max_length=5000)
    storage_condition = models.TextField(max_length=500)
    expiration = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def imageURL(self):
        if self.image:
            return self.image.url
        return ''

    def __str__(self):
        return self.name

class Comment(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='comment_user')
    subject = models.CharField(max_length=55, blank=True, null=True)
    comment = models.TextField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment