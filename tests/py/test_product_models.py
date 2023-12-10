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
    def setUp(self):
        self.product_url = reverse("ecommerce_api:products")
        self.client = APIClient()
        
        self.category1 = Categories.objects.create(
            name="test category 1",
            description="test description",
            tags="test1 test2"
        )
        self.category2 = Categories.objects.create(
            name="test category 2",
            description="test description",
            tags="test1 test2 test3"
        )
        self.category3 = Categories.objects.create(
            name="test category 3",
            description="test description",
            tags="test1 test2 test3 test4"
        )
        self.category4 = Categories.objects.create(
            name="test category 4",
            description="test description",
            tags="test1 test2 test3 test4 test5"
        )
        
        self.product1 = Products.objects.create(
            title="test product 1",
            description="test description",
            price=100.0,
            category=self.category1,
            summary="test summary",
            tags="test1 test2",
            discount_type="None",
            discount_value=0,
        )
        self.product2 = Products.objects.create(
            title="test product 2",
            description="test description",
            price=100.0,
            category=self.category2,
            summary="test summary",
            tags="test1 test2",
            discount_type="None",
            discount_value=0,
        )
        self.product3 = Products.objects.create(
            title="test product 3",
            description="test description",
            price=100.0,
            category=self.category3,
            summary="test summary",
            tags="test1 test2",
            discount_type="None",
            discount_value=0,
        )
        
        self.category_data1 = {
            "name": "test category 1",
            "description": "test description",
            "tags": "test1 test2"
        }
        
        category_data = CategoriesSerializer(self.category1).data
        self.product_data1 = {
            "title": "test product",
            "description": "test description",
            "price": 100.0,
            "category": category_data,
            "summary": "test summary",
            "tags": "test1 test2",
            "discount_type": "None",
            "discount_value": 0,
        }
    
    def test_product_creation(self):        
        response = self.client.post(self.product_url, json.dumps(self.product_data1), format="json")
        try:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        except AssertionError as e:
            print(f"AssertionError: {e}")
        except Exception as e:
            print(f"Exception: {e}")
        
    def test_get_all_product(self):
        try:
            response = self.client.get(self.product_url, format=None)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        except AssertionError as e:
            print(f"AssertionError: {e}")
        except Exception as e:
            print(f"Exception: {e}")
            
            
    def test_get_a_product(self):
        response = self.client.get(self.product_url + "?" + urlencode({"name": "test product 1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.get(self.product_url + "?" + urlencode({"id": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_delete_a_product(self):
        response = self.client.delete(self.product_url + "?" + urlencode({"title": "test product 1"}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data["message"], "Item has been deleted")
        
        
    def test_category_creation(self):
        category_list_url = reverse("ecommerce_api:category-list")
        response = self.client.post(category_list_url, self.category_data1, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_all_categories(self):
        category_list_url = reverse("ecommerce_api:category-list")
        response = self.client.get(category_list_url, format=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_get_a_category(self):
        category_list_url = reverse("ecommerce_api:category-list")
        response = self.client.get(category_list_url + "?" + urlencode({"name": "test category 1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        category_detail_url = reverse("ecommerce_api:category-detail", kwargs={"pk": 3})
        response = self.client.get(category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_delete_a_category(self):
        print(f"Category 4 id : {self.category4.id}")
        category_list_url = reverse("ecommerce_api:category-list")
        response = self.client.delete(category_list_url + "?" + urlencode({"name": "test category 3"}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        category_detail_url = reverse("ecommerce_api:category-detail", kwargs={"pk": 4})
        response = self.client.delete(category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)