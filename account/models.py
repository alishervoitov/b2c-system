from django.db import models
from django.contrib.auth.models import AbstractUser

COUNTRY_CHOICE = (
    ('UZBEKISTAN', 'uzbekistan'),
    ('KYRGIZISTAN', 'kyrgizistan'),
    ('KAZAKHSTAN', 'kazakhstan'),
    ('TURKMENISTAN', 'turkmenistan'),
    ('TADJIKISTAN', 'tadjikistan'),
)

class CustomerUser(AbstractUser):

    Customer = 'Customer'
    Provider = 'Provider'
    Both = 'Both'

    USER_TYPE_CHOICE = (
        ('Provider', 'provider'),
        ('Customer', 'customer'),
        ('Both', 'both'),
    )
    email = models.EmailField(
        max_length=100,
        unique=True
    )
    username = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=70,null=True, blank=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICE)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICE)
    phone_number = models.CharField(max_length=30)
    corporate_number = models.CharField(max_length=30, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number"]
    def __str__(self):
        return self.email