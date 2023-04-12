from rest_framework import serializers

from product.models import Product
from zakaz.models import OrderDetail


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ['id', 'quantity', 'product']

class CartItemAddSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()

    class Meta:
        model = OrderDetail
        fields = [
            'product_id'
        ]
