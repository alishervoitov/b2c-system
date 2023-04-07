from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from product.models import Product
from product.serializers import ProductSerializer


class ProductView(generics.ListAPIView):

    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]