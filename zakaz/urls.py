from django.urls import path
from zakaz.views import CartItemView, CartItemAddView, CartItemDelView

urlpatterns = [
    path('cart-item/', CartItemView.as_view(), name='cart-item'),
    path('add-item/', CartItemAddView.as_view(), name='add-item'),
    path('delete-item/', CartItemDelView.as_view(), name='delete-item'),
]