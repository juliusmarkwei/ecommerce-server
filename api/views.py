from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from user.models import CustomUser, SocialProfile, Credentials
from product.models import Products, Categories, Reviews
from cart.models import Carts, CartItems
from order.models import Orders, OrderLines
from rest_framework import generics
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError


# users views
class UsersView(APIView):
    permission_classes = [AllowAny]

    def get_queryset(self):
        users = CustomUser.objects.all()
        return users

    def get(self, request, *args, **kwargs):
        user_id = None
        try:
            user_id = request.query_params["id"]
            user = CustomUser.objects.get(id=user_id)
            serializer = serializers.CustomUserSerializer(user)
        except:
            print(f"User id {user_id} not found")
            users = self.get_queryset()
            serializer = serializers.CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_data = request.data
        try:
            user = CustomUser.objects.create_user(
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

    def delete(self, request, *args, **kwargs):
        if request.query_params.get("username") != None:
            username = request.query_params.get("username")
            print(username)
            try:
                user = CustomUser.objects.get(username=username)
                user.delete()

                return Response({"message": "User deleted successfully"})
            except CustomUser.DoesNotExist:
                return Response(
                    {"message": f"User with username '{username}' not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(
            {"message": "Provide a 'username' parameter to perform deletion"}
        )


class SocialProfileList(generics.ListCreateAPIView):
    queryset = SocialProfile.objects.all()
    serializer_class = serializers.SocialProfileSerializer
    permission_classes = [AllowAny]


class SocialProfileRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialProfile.objects.all()
    serializer_class = serializers.SocialProfileSerializer
    permission_classes = [AllowAny]


class CredentialsList(generics.ListCreateAPIView):
    queryset = Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer
    permission_classes = [AllowAny]


class CredentialsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer
    permission_classes = [AllowAny]


# product views
class ProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None, *args, **kwargs):
        print(request.user)
        if pk:
            try:
                product = Products.objects.get(pk=pk)
                serializer = serializers.ProductsSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Products.DoesNotExist:
                return Response(
                    {"message": f"Product with id {pk} not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            try:
                product_name = request.query_params["title"]
                product = Products.objects.get(title=product_name)
                serializer = serializers.ProductsSerializer(product)

                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                products = Products.objects.all()
                serializer = serializers.ProductsSerializer(products, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_data = request.data

        category_instance = Categories.objects.get(id=product_data["category"])
        try:
            product = Products.objects.create(
                title=product_data["title"],
                category=category_instance,
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
        except:
            return Response(
                "Required fields not provided!", status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk=None, *args, **kwargs):
        print(request.user)

        if pk != None:
            try:
                print("Product about to be queried")
                product = Products.objects.get(pk=pk)
                print("Product queried successfully")
            except Products.DoesNotExist:
                return Response(
                    {"message": f"Product with id {pk} not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        elif "title" in request.query_params:
            product_title = request.query_params.get("title")
            try:
                product = Products.objects.get(title=product_title)
            except Products.DoesNotExist:
                return Response(
                    {"message": f"Product with title '{product_title}' not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Provide the product 'id' or 'title' to delete an item"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        product.delete()
        return Response(
            {"message": "Item has been deleted"}, status=status.HTTP_204_NO_CONTENT
        )


class CategoriesList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if request.GET:
        # Do something if query parameters are present
            return Response(f"Query parameters found: {request.GET}")
        else:
            # Do something else if no query parameters are present
            return Response("No query parameters")


class CategoriesRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [AllowAny]


class ReviewList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = serializers.ReviewsSerializer
    permission_classes = [AllowAny]


class ReviewRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = serializers.ReviewsSerializer
    permission_classes = [AllowAny]


# order views
class OrderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = serializers.OrdersSerializer
    permission_classes = [AllowAny]


class OrderRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = serializers.OrdersSerializer
    permission_classes = [AllowAny]


class OrderLinesList(generics.ListCreateAPIView):
    queryset = OrderLines.objects.all()
    serializer_class = serializers.OrderLinesSerializer
    permission_classes = [AllowAny]


class OrderLinesRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderLines.objects.all()
    serializer_class = serializers.OrderLinesSerializer
    permission_classes = [AllowAny]


# cart views
class CartsList(generics.ListCreateAPIView):
    queryset = Carts.objects.all()
    serializer_class = serializers.CartsSerializer
    permission_classes = [AllowAny]


class CartsRetieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carts.objects.all()
    serializer_class = serializers.CartsSerializer
    permission_classes = [AllowAny]


class CartItemsList(generics.ListCreateAPIView):
    queryset = CartItems.objects.all()
    serializer_class = serializers.CartItemsSerializer
    permission_classes = [AllowAny]


class CartItemsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItems.objects.all()
    serializer_class = serializers.CartItemsSerializer
    permission_classes = [AllowAny]
