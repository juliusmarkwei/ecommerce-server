from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, BasePermission
from src.user.models import CustomUser
from src.product.models import Products, Categories, Reviews
from src.cart.models import Carts, CartItems
from src.order.models import Orders, OrderLines
from rest_framework import generics
from .serializers import (
    CustomUserSerializer,
    ReviewsSerializer,
    OrdersSerializer,
    OrderLinesSerializer,
    CartsSerializer,
    CartItemsSerializer,
    CategoriesSerializer,
    ProductsSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.utils import IntegrityError
from .permissions import *
from rest_framework.exceptions import PermissionDenied



# users views
class UsersView(APIView):
    # permission_classes = [AllowAny]
        
    # def get_permissions(self):
    #     if self.request.method == "POST":
    #         return [AllowPostRequests()]
    #     elif self.request.method == "GET":
    #         return [IsAdminUserOrReadOnly()]
    #     return super().get_permissions()


    def get_queryset(self):
        users = CustomUser.objects.all()
        return users

    def get(self, request, pk=None, *args, **kwargs):
        # print(request.user)
        if pk:
            try:
                user = CustomUser.objects.get(pk=pk)
                serializer = CustomUserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response(
                    {"message": f"Product with id {pk} not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            if request.query_params:
                if "username" in request.query_params:
                    try:
                        username = request.query_params["username"]
                        user = CustomUser.objects.get(username=username)
                        
                    except ObjectDoesNotExist:
                        return Response({"error": f"user '{username}' does not exist"}, status=status.HTTP_400_BAD_REQUEST)
                elif "id" in request.query_params or "pk" in request.query_params:
                    try:
                        user_id = request.query_params["id"]
                        user = CustomUser.objects.get(id=user_id)
                        
                    except ObjectDoesNotExist:
                        return Response({"error": f"User ID '{user_id}' does not exist"}, status=status.HTTP_400_BAD_REQUEST)
                    
                serializer = CustomUserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        users = CustomUser.objects.all()
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
        except KeyError as e:
            return Response({"error": f"Provide key(s) {e}"}, status.HTTP_400_BAD_REQUEST)
        
        except IntegrityError as e:
            return Response({"error": f"{e}"})
        user.save()
        
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        if request.query_params.get("username") is not None:
            username = request.query_params.get("username")
            try:
                user = CustomUser.objects.get(username=username)
                # Manually check for permission
                # self.check_object_permissions(request, user)
                user.delete()
                return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except CustomUser.DoesNotExist:
                return Response({"message": f"User '{username}' not found"}, status=status.HTTP_404_NOT_FOUND)
            except PermissionDenied:
                return Response({"message": "You do not have permission to delete this user"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "Provide a 'username' parameter to perform deletion"})



# product views
class ProductsView(APIView):
    # permission_classes = [AllowAny]

    def get(self, request, pk=None, *args, **kwargs):
        print(request.method)
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

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                f"{e}", status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk=None, *args, **kwargs):
        # print(request.user)

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
    # permission_classes = [AllowAny]

    def get(self, request, pk=None, *args, **kwargs):
        # print(request.user)
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
                    return Response({"message": f"Category with name '{category_name}' not found."}                    )
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

        category.save()
        serializer = CategoriesSerializer(category)

        return Response(serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, pk=None, *args, **kwargs):
        category = None
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
            {"success": "Category item deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class ReviewView(APIView):
    # permission_classes = [AllowAny]

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                review = Reviews.objects.get(id=pk)
            except ObjectDoesNotExist:
                return Response(
                    {"error": f"You provided an invalid id '{pk}.'"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        elif request.query_params:
            if "product" in request.query_params:
                product_name = request.query_params.get("product")
                try:
                    review = Reviews.objects.get(product=product_name)
                except ObjectDoesNotExist:
                    return Response(
                        {"error": f"Invalid product name '{product_name}'"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {
                        "error": f"Provide 'name' as key with a value (Category name) to select a product."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if pk or request.query_params:
            serializer = ReviewsSerializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)

        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # print(request.user)
        user_id = CustomUser.objects.get(username=request.user)
        product = Products.objects.get(title=request.data["product"])

        review_data = request.data
        try:
            review = Reviews.objects.create(
                user=user_id,
                product=product,
                rating=review_data["rating"],
                comments=review_data["comments"],
            )
        except KeyError as e:
            return Response(
                {"error": f"Provide key(s) {e}"}, status=status.HTTP_400_BAD_REQUEST
            )
        review.save()

        serializer = ReviewsSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# order views
class OrdersView(APIView):
    # permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        username = request.user
        print(username)
        
        order = Orders.objects.create(user=username)
        order.save()
        serializer = OrdersSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, pk=None, *args, **kwargs):
        # print(request.user)
        if pk:
            try:
                order = Orders.objects.get(id=pk)
            except ObjectDoesNotExist:
                return Response(
                    {"error": f"You provided an invalid id '{pk}.'"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        elif request.query_params:
            if "username" in request.query_params:
                username = request.query_params.get("username")
                try:
                    order = Orders.objects.get(user=username)
                except ObjectDoesNotExist:
                    return Response(
                        {"error": f"Invalid username name '{username}'"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {
                        "error": f"Provide 'username' as key with a value (user's username) to select a review."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if pk or request.query_params:
            serializer = ReviewsSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderLinesView(APIView):
    # permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        try:
            order = Orders.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response({"error": f"Order hasn't been created by user '{request.user}'"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            product = Products.objects.get(title=request.data["product"])
        except ObjectDoesNotExist:
            return Response({"error": f"Product '{request.data['product']}' not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            orderLine = OrderLines.objects.create(
                order=order,
                product=product,
                price=product.price,
                quantity=request.data["quantity"]
            )
        except KeyError as e:
            return Response({"error": f"Provide key(s) {e}"}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            orderLine = OrderLines.objects.get(order=order, product=product)
            orderLine.quantity += int(request.data["quantity"])
            orderLine.save()

        serializer = OrderLinesSerializer(orderLine)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def get(self, request, *args, **kwargs):
        if request.query_params:
            if "product" in request.query_params:
                product_name = request.query_params['product']
                
                try:
                    # product = Products.objects.get(title=product_name).id
                    orderLines = OrderLines.objects.filter(product=product_name)
                    
                    many = orderLines.count() > 1
                    serializer = OrderLinesSerializer(orderLines, many=many)
                    return Response(serializer.data, status=status.HTTP_200_OK)

                except Products.DoesNotExist:
                    return Response({"error": f"Product with title '{product_name}' does not exist."}, status=status.HTTP_404_NOT_FOUND)
                    
                serializer = OrderLinesSerializer(product_name)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            else:
                keys = [key for key in request.query_params.keys()]
                return Response({"error": f"Provide key(s) '{keys}'"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            orderLines = OrderLines.objects.all()
            serializer = OrderLinesSerializer(orderLines, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, format=None):
        product = request.data["product"]
        order = request.data["order"]
        
        try:
            orderLine = OrderLines.objects.get(product=product, order=order)
            orderLine.delete()
            return Response({"message": "Order line deleted successfully"}, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({"error": "Order line not found"}, status=status.HTTP_404_NOT_FOUND)
        
        except MultipleObjectsReturned:
            return Response({"error": "Multiple order lines found (data integrity issue)"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

# cart views
class CartsView(APIView):
    # permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        created_by = request.user
        try:
            cart = Carts.objects.create(
                created_by=created_by,
                status=request.data["status"]
            )
        except KeyError as e:
            return Response({"error": f"Provide key(s) {e}"}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"error": f"Cart already exist for user '{created_by}'"})
        cart.save()
        serializer = CartsSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        user = request.user
        
        if request.query_params:
            if "username" in request.query_params:
                try:
                    cart = Carts.objects.filter(created_by=user)
                except ObjectDoesNotExist:
                    return Response({"error": f"User '{user}' has no cart"})
            
            elif "status" in request.query_params:
                try:
                    cart = Carts.objects.filter(status=request.query_params.get("status"))
                except ObjectDoesNotExist:
                    return Response({"error": f"User '{user}' has no cart"}, status=status.HTTP_400_BAD_REQUEST)
                
            many = cart.count() > 1
            serializer = CartsSerializer(cart, many=many)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        carts = Carts.objects.all()
        serializer = CartsSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    def delete(self, request, *args, **kwargs):
        user = request.user
        try:
            cart = Carts.objects.get(created_by=user)
            cart.delete()
            return Response({"message": "Cart deleted successfully"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": f"User '{user}' has no cart"}, status=status.HTTP_400_BAD_REQUEST)


class CartItemsView(APIView):
    # permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            cart_id = Carts.objects.get(created_by=user)
        except ObjectDoesNotExist:
            return Response({"error": f"User '{user}' has no cart"})
        product_id = Products.objects.get(title=request.data["product"])
        
        try:
            cartItem = CartItems.objects.create(
                cart_id=cart_id,
                product_id=product_id,
                price=product_id.price,
                quantity=request.data["quantity"],
            )
        except KeyError as e:
            return Response({"error": f"Provide key {e}"}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            quantity = request.data["quantity"]
            cartItem = CartItems.objects.get(cart_id=cart_id, product_id=product_id)
            cartItem.quantity += quantity
            cartItem.save()
        cartItem.save()
        serializer = CartItemsSerializer(cartItem)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)

        if request.query_params:
            if "product" in request.query_params:
                product_name = request.query_params.get("product")
                try:
                    product = Products.objects.get(title=product_name)
                    cartItem = CartItems.objects.filter(product_id=product)
                except ObjectDoesNotExist:
                    return Response({"error": f"Product '{product_name}' not found"}, status=status.HTTP_404_NOT_FOUND)
                
                many = cartItem.count() >= 1
                print(many)
                serializer = CartItemsSerializer(cartItem, many=many)
                
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                keys = [key for key in request.query_params.keys()]
                return Response({"error": f"Provide key(s) '{keys}'"}, status=status.HTTP_400_BAD_REQUEST)
        
        cartItems = CartItems.objects.all()
        serializer = CartItemsSerializer(cartItems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
