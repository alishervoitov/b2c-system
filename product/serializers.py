from rest_framework import serializers

from product.models import Product, Category, Comment, Rating


class RatingSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()
    class Meta:
        model = Rating
        fields = [
            'product_id',
            # 'user',
            'star',
        ]


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



class CommentSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = [
            'product_id',
            'comment',
            # 'user'
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
            'comment',
        ]

