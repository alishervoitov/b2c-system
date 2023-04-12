from django.shortcuts import render
from django_filters import filters
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from zakaz.models import OrderDetail
from zakaz.serializers import CartItemSerializer, CartItemAddSerializer


class CartItemView(generics.ListAPIView):

    serializer_class = CartItemSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'product__name', 'product__description', 'product__category__name']

    def get_queryset(self):
        user = self.request.user
        return OrderDetail.objects.filter(user=user)

class CartItemAddView(APIView):

    queryset = OrderDetail.objects.all()
    serializer_class = CartItemAddSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):

        user = request.user
        product = Product.objects.get(id=request.data['product_id'])

        order_detail = OrderDetail.objects.filter(
            user=user,
            product=product
        ).first()
        if order_detail:
            order_detail.delete()
            return Response({
                'Message': 'Product has got in cart item'
            })
        else:
            order_detail = OrderDetail.objects.create(
                user=user,
                product=product,
            )
            order_detail.save()
            return Response({
                'Message': 'Product added to cart'
            },
                status=status.HTTP_201_CREATED
            )