from rest_framework.serializers import ModelSerializer
from src.user.models import CustomUser
from src.product.models import Products, Categories, Reviews
from src.cart.models import Carts, CartItems
from src.order.models import Orders, OrderLines
from collections import OrderedDict
from rest_framework import serializers


# user serializer
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "phone",
            "role",
            "username",
            "first_name",
            "last_name",
            "avatar",
            "locale",
            "bio",
            "company",
        ]
        


class CustomUserPOSTSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "phone",
            "role",
            "username",
            "first_name",
            "last_name",
            "password",
            "avatar",
            "locale",
            "bio",
            "company",
        ]

# product serializer
class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "id",
            "category",
            "title",
            "picture",
            "summary",
            "description",
            "price",
            "discount_type",
            "discount_value",
            "created_at",
            "updated_at",
        ]


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = [
            "id",
            "parent_category",
            "slug",
            "name",
            "description",
            "tags",
            "created_at",
            "updated_at",
        ]
        


class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ["id", "user_id", "product", "rating", "comments", "created_at"]

    
# Oder serializer
class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id", "user", "created_at"]
        

class OrderLinesSerializer(ModelSerializer):
    class Meta:
        model = OrderLines
        fields = ["id", "order", "product", "price", "quantity"]
        

class CartsSerializer(ModelSerializer):
    class Meta:
        model = Carts
        fields = ["id", "created_by", "status", "created_at", "updated_at"]
        

class CartItemsSerializer(ModelSerializer):
    class Meta:
        model = CartItems
        fields = ["id", "product_id", "price", "cart_id", "quantity", "created_at"]

        
        
class CartStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Carts.status_options)