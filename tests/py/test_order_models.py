# testing orders CRUD

from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from src.order.models import Orders, OrderLines
from src.user.models import CustomUser
from src.product.models import Products, Categories
from urllib.parse import urlencode
from rest_framework import status
from api.serializers import ProductsSerializer, OrdersSerializer, CustomUserSerializer, CategoriesSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from api.serializers import CustomUserSerializer, OrdersSerializer, OrderLinesSerializer


class TestOrderModels(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.User = get_user_model()
        self.user1 = self.User.objects.create_user(
            username="testuser1",
            password="test123",
            first_name="Dora",
            last_name="Maldonado",
            email="soj@fi.vn",
            phone="(312) 515-6977",
        )
        self.client.login(username="testuser1", password="test123")
        self.order1 = Orders.objects.create(user=self.user1)
        self.user1_data_serialized = CustomUserSerializer(self.user1).data
        # self.user1_data = CustomUserSerializer(self.user1).data
        self.order_data1 = {"user": self.user1_data_serialized}
        # self.order_data1_serialized = OrdersSerializer(self.order1).data
        
        # self.category1 = Categories.objects.create(
        #     name="Category 1",
        #     description="Category 1 description",
        #     tags="category1 category2",
        # )
        
        # # self.category1_data = CategoriesSerializer(self.category1).data
        
        # self.product1 = Products.objects.create(
        #     category=self.category1,
        #     title="Product 1",
        #     summary="Product 1 summary",
        #     description="Product 1 description",
        #     price=100.00,
        #     discount_type="None",
        #     discount_value=0.0,
        #     tags="product1 product2",
        # )
        # self.product2 = Products.objects.create(
        #     category=self.category1,
        #     title="Product 2",
        #     summary="Product 2 summary",
        #     description="Product 2 description",
        #     price=70.00,
        #     discount_type="None",
        #     discount_value=0.0,
        #     tags="product1 product2 product3",
        # )
        # self.product1_data_serilized = ProductsSerializer(self.product1).data
        
        # self.order_line1 = OrderLines.objects.create(
        #     product=self.product1,
        #     order=self.order1,
        #     price=60,
        #     quantity=1
        # )
        # self.order_line2 = OrderLines.objects.create(
        #     product=self.product2,
        #     order=self.order1,
        #     price=900,
        #     quantity=4
        # )
        
        
        # self.order_line_data1 = {
        #     "product": self.product1_data_serilized,
        #     "order": self.order_data1_serialized,
        #     "price": 5000.00,
        #     "quantity": 1
        # }
        
        # self.order_line1_serialized = OrderLinesSerializer(self.order_line1).data
        # self.order_line_to_delete = {
        #     "product": self.order_line1_serialized.get("product"),
        #     "order": self.order_line1_serialized.get("order")
        # }
        
    # def test_order_creation(self):
    #     order_url = reverse("ecommerce_api:order-list")
    #     response = self.client.post(order_url, self.order_data1, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    # def test_get_all_orders(self):
    #     order_url = reverse("ecommerce_api:order-list")
    #     response = self.client.get(order_url, format=None)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    # def test_get_a_order(self):
    #     order_url = reverse("ecommerce_api:order-list")
    #     response = self.client.get(order_url + "?" + urlencode({"username": self.order1.user}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    #     order_url = reverse("ecommerce_api:order-detail", kwargs={"pk": self.order1.pk})
    #     response = self.client.get(order_url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    # def test_order_deletion(self):
    #     order_url = reverse("ecommerce_api:order-detail", kwargs={"pk": self.order1.pk})
    #     response = self.client.delete(order_url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    #     order_url = reverse("ecommerce_api:order-list")
    #     response = self.client.delete(order_url + "?" + urlencode({"username": self.user1.username}))
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(response.data["message"], "Order deleted successfully")
        
    # # def test_order_line_creation(self):
    # #     order_line_url = reverse("ecommerce_api:order-lines")
    # #     response = self.client.post(order_line_url, self.order_line_data1, format="json")
    # #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

    # def test_get_all_order_lines(self):
    #     order_lines_url = reverse("ecommerce_api:order-lines")
    #     response = self.client.get(order_lines_url, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    # def test_get_a_order_line(self):
    #     order_line_url = reverse("ecommerce_api:order-lines")
    #     response = self.client.get(order_line_url + "?" + urlencode({"product": self.order_line1.product}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    # def test_order_line_deletion(self):
    #     order_line_url = reverse("ecommerce_api:order-lines")
    #     response = self.client.delete(order_line_url, self.order_line_to_delete)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        