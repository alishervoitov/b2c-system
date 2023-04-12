from django.shortcuts import render
from django_filters import filters
from rest_framework import generics, permissions

from zakaz.models import OrderDetail
from zakaz.serializers import CartItemSerializer


class CartItemView(generics.ListAPIView):

    serializer_class = CartItemSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'product__name', 'product__description', 'product__category__name']

    def get_queryset(self):
        user = self.request.user
        return OrderDetail.objects.filter(user=user)