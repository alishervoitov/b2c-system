from rest_framework import serializers

from product.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'company',
            'price',
            'medicine_form',
        ]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'company',
            'price',
            'medicine_form',
            'category',
            'image',
            'company',
            'country',
            'active_ingredient',
            'composition',
            'pharmacotherapeutic_group',
            'contraindication',
            'storage_condition',
        ]