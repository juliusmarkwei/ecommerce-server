from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from user import models as user_models
from product import models as product_models
from cart import models as cart_models
from order import models as order_models
from rest_framework import generics
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


# users views
class UsersView(APIView):
    permission_classes = [AllowAny]

    def get_queryset(self):
        users = user_models.CustomUser.objects.all()
        return users

    def get(self, request, *args, **kwargs):
        user_id = None
        try:
            user_id = request.query_params["id"]
            user = user_models.CustomUser.objects.get(id=user_id)
            serializer = serializers.CustomUserSerializer(user)
        except:
            print(f"User id {user_id} not found")
            users = self.get_queryset()
            serializer = serializers.CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_data = request.data
        try:
            user = user_models.CustomUser.objects.create_user(
                email=user_data["email"],
                username=user_data["username"],
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                password=user_data["password"],
                phone=user_data["phone"],
            )
            user.save()
            serializer = serializers.CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response("Error rasies during user creation")


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
class ProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            product_name = request.query_params["title"]
            product = product_models.Products.objects.get(title=product_name)
            serializer = serializers.ProductsSerializer(product)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            products = product_models.Products.objects.all()
            serializer = serializers.ProductsSerializer(products, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_data = request.data
        # try:
        product = product_models.Products.objects.create(
            title=product_data["title"],
            category=product_data["category"],
            description=product_data["description"],
            tags=product_data["tags"],
            summary=product_data["summary"],
            price=product_data["price"],
            discount_type=product_data["discount_type"],
            discount_value=product_data["discount_value"],
        )
        product.save()
        serializer = serializers.ProductsSerializer(product)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # except:
        #     return Response("Post Request received",status=status.HTTP_400_BAD_REQUEST)


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
