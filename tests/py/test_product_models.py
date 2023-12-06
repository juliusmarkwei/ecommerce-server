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
        
        