# testing product CRUD

from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from src.user.models import CustomUser
from src.product.models import Products, Categories, Reviews


class TestProduct(APITestCase):
    url = "ecommerce-api:products"
    client = APIClient()
    
    def test_product_creation(self):
        testuser1 = CustomUser.objects.create_user(
            username="testuser1",
            first_name="Leo",
            last_name="Mack",
            password="testpass123",
            email="jowutaaku@maznuki.bs",
            phone="(973) 419-1448"
        )
        
        self.client.login(username=testuser1, password=testuser1.password)
        
        category = Categories.objects.create(
            name="test category",
            description="test description",
            tags="test1 test2"
        )
        
        product = Products.objects.create(
            title="test product",
            description="test description",
            price=100,
            category=category,
            summary="test summary",
            tags="test1 test2",
            discount_type="test discount type",
            discount_value=0,
        )
        
        data = {
            ""
        }
        
        response = self.client.post(self.url, product, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)
        
        