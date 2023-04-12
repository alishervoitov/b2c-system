from django.shortcuts import render
from rest_framework import generics, permissions

from zakaz.models import OrderDetail
from zakaz.serializers import CartItemSerializer


class CartItemView(generics.ListAPIView):

    serializer_class = CartItemSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return OrderDetail.objects.filter(user=user)