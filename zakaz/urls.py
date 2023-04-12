from django.urls import path
from zakaz.views import CartItemView

urlpatterns = [
    path('cart-item/', CartItemView.as_view(), name='cart-item'),
]