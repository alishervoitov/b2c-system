from django.urls import path
from product.views import ProductView, ProductDetailView, CategoryView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryView.as_view(), name='categories'),
]