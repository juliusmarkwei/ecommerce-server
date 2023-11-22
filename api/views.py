from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from user import models as user_models
from product import models as product_models
from cart import models as cart_models
from order import models as order_models
from rest_framework import generics
from . import serializers
from django.shortcuts import get_object_or_404


# users views
class UsersList(generics.ListCreateAPIView):
    queryset = user_models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [AllowAny]


class UsersRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [AllowAny]


class SocialProfileList(generics.ListCreateAPIView):
    queryset = user_models.SocialProfile.objects.all()
    serializer_class = serializers.SocialProfileSerializer
    permission_classes = [AllowAny]


class SocialProfileRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_models.SocialProfile.objects.all()
    serializer_class = serializers.SocialProfileSerializer
    permission_classes = [AllowAny]


class CredentialsList(generics.ListCreateAPIView):
    queryset = user_models.Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer
    permission_classes = [AllowAny]


class CredentialsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_models.Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer
    permission_classes = [AllowAny]


# product views
class ProductList(generics.ListAPIView):
    queryset = product_models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [AllowAny]


class ProductRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [AllowAny]


class CategoriesList(generics.ListCreateAPIView):
    queryset = product_models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [AllowAny]


class CategoriesRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [AllowAny]


class ReviewList(generics.ListCreateAPIView):
    queryset = product_models.Reviews.objects.all()
    serializer_class = serializers.ReviewsSerializer
    permission_classes = [AllowAny]


class ReviewRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Reviews.objects.all()
    serializer_class = serializers.ReviewsSerializer
    permission_classes = [AllowAny]


# order views
class OrderList(generics.ListCreateAPIView):
    queryset = order_models.Orders.objects.all()
    serializer_class = serializers.OrdersSerializer
    permission_classes = [AllowAny]


class OrderRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = order_models.Orders.objects.all()
    serializer_class = serializers.OrdersSerializer
    permission_classes = [AllowAny]


class OrderLinesList(generics.ListCreateAPIView):
    queryset = order_models.OrderLines.objects.all()
    serializer_class = serializers.OrderLinesSerializer
    permission_classes = [AllowAny]


class OrderLinesRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = order_models.OrderLines.objects.all()
    serializer_class = serializers.OrderLinesSerializer
    permission_classes = [AllowAny]


# cart views
class CartsList(generics.ListCreateAPIView):
    queryset = cart_models.Carts.objects.all()
    serializer_class = serializers.CartsSerializer
    permission_classes = [AllowAny]


class CartsRetieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = cart_models.Carts.objects.all()
    serializer_class = serializers.CartsSerializer
    permission_classes = [AllowAny]


class CartItemsList(generics.ListCreateAPIView):
    queryset = cart_models.CartItems.objects.all()
    serializer_class = serializers.CartItemsSerializer
    permission_classes = [AllowAny]


class CartItemsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = cart_models.CartItems.objects.all()
    serializer_class = serializers.CartItemsSerializer
    permission_classes = [AllowAny]
