from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from src.user.models import CustomUser, SocialProfile, Credentials
from src.product.models import Products, Categories, Reviews
from src.cart.models import Carts, CartItems
from src.order.models import Orders, OrderLines
from rest_framework import generics
from .serializers import (
    CustomUserSerializer,
    SocialProfileSerializer,
    CredentialsSerializer,
    ReviewsSerializer,
    OrdersSerializer,
    OrderLinesSerializer,
    CartsSerializer,
    CartItemsSerializer,
    CategoriesSerializer,
    ProductsSerializer
)
from rest_framework.response import Response
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError


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
            serializer = CustomUserSerializer(user)
        except:
            print(f"User id {user_id} not found")
            users = self.get_queryset()
            serializer = CustomUserSerializer(users, many=True)
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
            serializer = CustomUserSerializer(user)
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
    serializer_class = SocialProfileSerializer
    permission_classes = [AllowAny]


class SocialProfileRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialProfile.objects.all()
    serializer_class = SocialProfileSerializer
    permission_classes = [AllowAny]


class CredentialsList(generics.ListCreateAPIView):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer
    permission_classes = [AllowAny]


class CredentialsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer
    permission_classes = [AllowAny]


# product views
class ProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None, *args, **kwargs):
        print(request.user)
        if pk:
            try:
                product = Products.objects.get(pk=pk)
                serializer = ProductsSerializer(product)
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
                serializer = ProductsSerializer(product)

                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                products = Products.objects.all()
                serializer = ProductsSerializer(products, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_data = request.data

        try:
            try:
                category_instance = Categories.objects.get(id=product_data["category"])
            except ObjectDoesNotExist:
                category_instance = None
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
            serializer = ProductsSerializer(product)

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


class CategoriesViews(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None, *args, **kwargs):
        print(request.user)
        if pk:
            try:
                category = Categories.objects.get(id=pk)
                serializer = CategoriesSerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(
                    {"message": f"Category with id {pk} not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        if request.query_params:
            if "name" in request.query_params:
                category_name = request.query_params.get("name")
                try:
                    category = Categories.objects.get(name=category_name)
                    serializer = CategoriesSerializer(category)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Categories.DoesNotExist:
                    return Response(
                        {"message": f"Category with name '{category_name}' not found."}
                    )
            else:
                return Response(
                    {
                        "message",
                        "Provide 'name' as key with a value to query for an item.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        category = Categories.objects.all()
        serializer = CategoriesSerializer(category, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        category_data = request.data
        try:
            try:
                parent_category_instance = Categories.objects.get(
                    id=category_data["parent_category"]
                )
            except (ObjectDoesNotExist, KeyError):
                parent_category_instance = None

            category = Categories.objects.create(
                parent_category=parent_category_instance,
                name=category_data["name"],
                description=category_data["description"],
                tags=category_data["tags"],
            )
        except KeyError as e:
            return Response(
                {"error": f"Missing field: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError:
            return Response(
                {
                    "error": f"Category name '{category_data['name']}' already exists in the database"
                },
                status=status.HTTP_409_CONFLICT,
            )

        print("----------------saving object into database----------------")
        category.save()
        serializer = CategoriesSerializer(category)

        return Response(
            {{"message": "Data sent successfully"}, {"data": serializer.data}},
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                category = Categories.objects.get(id=pk)
            except ObjectDoesNotExist:
                return Response(
                    {
                        "error": f"Category item with if {pk} does not exist. Provide a valid 'ID' or a 'name'"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif request.query_params:
            if "name" in request.query_params:
                category_name = request.query_params.get("name")
                try:
                    category = Categories.objects.get(name=category_name)
                except ObjectDoesNotExist:
                    return Response({"error": f"Invalid category name {category_name}"})
            else:
                return Response(
                    {
                        "error": f"Provide 'name' as key with a value (Category name) to remove the item."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        category.delete()
        return Response(
            {"success": "Category item deleted successfully"}, status=status.HTTP_200_OK
        )


class ReviewView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        pass


class ReviewRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [AllowAny]


# order views
class OrderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [AllowAny]


class OrderRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [AllowAny]


class OrderLinesList(generics.ListCreateAPIView):
    queryset = OrderLines.objects.all()
    serializer_class = OrderLinesSerializer
    permission_classes = [AllowAny]


class OrderLinesRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderLines.objects.all()
    serializer_class = OrderLinesSerializer
    permission_classes = [AllowAny]


# cart views
class CartsList(generics.ListCreateAPIView):
    queryset = Carts.objects.all()
    serializer_class = CartsSerializer
    permission_classes = [AllowAny]


class CartsRetieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carts.objects.all()
    serializer_class = CartsSerializer
    permission_classes = [AllowAny]


class CartItemsList(generics.ListCreateAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer
    permission_classes = [AllowAny]


class CartItemsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer
    permission_classes = [AllowAny]
