from rest_framework.serializers import ModelSerializer
from user import models as user_models
from product import models as product_models
from cart import models as cart_models
from order import models as order_models


# user serializer
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = user_models.CustomUser
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


class SocialProfileSerializer(ModelSerializer):
    class Meta:
        model = user_models.SocialProfile
        fields = ["id", "user_id", "platform", "platform_user"]


class CredentialsSerializer(ModelSerializer):
    class Meta:
        model = user_models.Credentials
        fields = [
            "id",
            "provider_id",
            "provider_key",
            "user_id",
            "hasher",
            "password_hash",
            "password_salt",
        ]


# product serializer
class ProductsSerializer(ModelSerializer):
    class Meta:
        model = product_models.Products
        fields = [
            "category",
            "title",
            "picture",
            "summary",
            "description",
            "price",
            "discount_type",
            "discount_value",
            "tags",
            "created_at",
            "updated_at",
        ]


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = product_models.Categories
        fields = [
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
        model = product_models.Reviews
        fields = ["id", "user_id", "product", "rating", "comments", "created_at"]


# Oder serializer
class OrdersSerializer(ModelSerializer):
    class Meta:
        model = order_models.Orders
        fields = ["user", "created_at"]


class OrderLinesSerializer(ModelSerializer):
    class Meta:
        model = order_models.OrderLines
        fields = ["id", "order", "product", "price", "quantity"]


class CartsSerializer(ModelSerializer):
    class Meta:
        model = cart_models.Carts
        fields = ["id", "created_by", "status", "created_at", "updated_at"]


class CartItemsSerializer(ModelSerializer):
    class Meta:
        model = cart_models.CartItems
        fields = ["id", "cart_id", "product_id", "quantity", "created_at"]
