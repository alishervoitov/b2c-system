from django.urls import path
from zakaz.views import CartItemView, CartItemAddView, CartItemDelView, CartItemAddOneView, CartItemReduceOneView

urlpatterns = [
    path('cart-item/', CartItemView.as_view(), name='cart-item'),
    path('add-item/', CartItemAddView.as_view(), name='add-item'),
    path('delete-item/', CartItemDelView.as_view(), name='delete-item'),
    path('add-one/', CartItemAddOneView.as_view(), name='add-one'),
    path('reduce-one/', CartItemReduceOneView.as_view(), name='reduce-one'),
]