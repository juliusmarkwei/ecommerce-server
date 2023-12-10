# testing carts CRUD

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from src.cart.models import Carts, CartItems


class TestCart(APITestCase):
    def setUp(self):
        self.client = APIClient()
        
        
    def test_cart_creation(self):
        pass
    
    def test_cart_retrieval(self):
        pass
    
    def test_cart_update(self):
        pass
    
    def test_cart_deletion(self):
        pass