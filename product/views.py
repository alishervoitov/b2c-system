from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import Product, Category, Comment, Rating
from product.serializers import ProductSerializer, ProductDetailSerializer, CategorySerializer, CommentSerializer, \
    RatingSerializer


class CategoryView(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductView(generics.ListAPIView):

    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category_id', 'name', 'country']
    search_fields = ['name']
    pagination_class = PageNumberPagination

class ProductDetailView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            obj = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductDetailSerializer(obj)
        return Response(serializer.data)

class CommentView(generics.ListAPIView, generics.GenericAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):

        user = request.user
        product = Product.objects.get(id=request.data['product_id'])
        comment = request.data['comment']

        comments = Comment.objects.create(
            user=user,
            product=product,
            comment=comment,
        )
        comments.save()
        return Response(status=status.HTTP_200_OK)


class AddStarRatingView(generics.ListAPIView):

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        user = request.user
        product = Product.objects.get(id=request.data['product_id'])
        star = request.data['star']

        ratingss = Comment.objects.create(
            user=user,
            product=product,
            star=star,
        )
        ratingss.save()
        return Response(status=status.HTTP_200_OK)
