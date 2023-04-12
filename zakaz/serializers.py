from rest_framework import serializers

from product.models import Product
from zakaz.models import OrderDetail


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ['id', 'quantity', 'product']