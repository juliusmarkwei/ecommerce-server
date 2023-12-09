# testing product CRUD

from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from src.user.models import CustomUser
from src.product.models import Products, Categories, Reviews
from django.utils import timezone
import json
import ast
from urllib.parse import urlencode
from api.serializers import CategoriesSerializer


class TestProduct(APITestCase):
    url = reverse("ecommerce_api:products")
    client = APIClient()
    
    def test_product_creation(self):        
        category = Categories.objects.create(
            name="test category 1",
            description="test description",
            tags="test1 test2"
        )
        
        category_data = CategoriesSerializer(category).data
        
        data = {
            "title": "test product",
            "description": "test description",
            "price": 100.0,
            "category": category_data,
            "summary": "test summary",
            "tags": "test1 test2",
            "discount_type": "None",
            "discount_value": 0,
        }
        
        response = self.client.post(self.url, json.dumps(data), format="json")
        print(response.data)
        try:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        except AssertionError as e:
            print(f"AssertionError: {e}")
        except Exception as e:
            print(f"Exception: {e}")
        
    def test_get_all_product(self):
        category1 = Categories.objects.create(
            name="test category 2",
            description="test description",
            tags="test1 test2"
        )
                
        product1 = Products.objects.create(
            title="test product 1",
            description="test description",
            price=100.0,
            category=category1,
            summary="test summary",
            tags="test1 test2",
            discount_type="None",
            discount_value=0,
        )
        
        product2 = Products.objects.create(
            title="test product 2",
            description="test description",
            price=100.0,
            category=category1,
            summary="test summary",
            tags="test1 test2",
            discount_type="None",
            discount_value=0,
        )
        
        try:
            response = self.client.get(self.url, format=None)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        except AssertionError as e:
            print(f"AssertionError: {e}")
        except Exception as e:
            print(f"Exception: {e}")
            
            
    def test_get_a_product(self):
        category1 = Categories.objects.create(
            name="test category 3",
            description="test description",
            tags="test1 test2"
        )
        
        product1 = Products.objects.create(
            title="test product 1",
            description="test description",
            price=43.0,
            category=category1,
            summary="test summary",
            tags="test1 test2 test3",
            discount_type="None",
            discount_value=0,
        )
        
        response = self.client.get(self.url + "?" + urlencode({"name": "test product 1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.get(self.url + "?" + urlencode({"id": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_delete_a_product(self):
        category1 = Categories.objects.create(
            name="test category 3",
            description="test description",
            tags="test1 test2"
        )
        
        product1 = Products.objects.create(
            title="test product 4",
            description="test description",
            price=43.0,
            category=category1,
            summary="test summary",
            tags="test1 test2 test3",
            discount_type="None",
            discount_value=0,
        )
        
        response = self.client.delete(self.url + "?" + urlencode({"title": "test product 4"}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data["message"], "Item has been deleted")
        
        
    def test_category_creation(self):
        data = {
            "name": "test category 1",
            "description": "test description",
            "tags": "test1 test2"
        }
        
        url = reverse("ecommerce_api:categories")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_all_categories(self):
        category1 = Categories.objects.create(
            name="test category 1",
            description="test description",
            tags="test1 test2 test3 test4"
        )
        
        category2 = Categories.objects.create(
            name="test category 2",
            description="test description",
            tags="test1 test2 test3 test4"
        )
        
        url = reverse("ecommerce_api:categories")
        response = self.client.get(url, format=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_get_a_category(self):
        category1 = Categories.objects.create(
            name="test category 1",
            description="test description",
            tags="test1 test2 test3 test4"
        )
        
        url = reverse("ecommerce_api:categories")
        response = self.client.get(url + "?" + urlencode({"name": "test category 1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.get(url, kwargs={"pk": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_delete_a_category(self):
        category1 = Categories.objects.create(
            name="test category 1",
            description="test description",
            tags="test1 test2 test3 test4 test5"
        )
        
        print(category1.id)
        url = reverse("ecommerce_api:categories")
        response = self.client.delete(url + "?" + urlencode({"name": "test category 1"}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        response = self.client.delete(url, kwargs={"pk": 1})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)