from django.urls import path
from product.views import ProductView, ProductDetailView, CategoryView, CommentView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('comments/', CommentView.as_view(), name='comments'),
]