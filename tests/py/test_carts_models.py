# testing carts CRUD

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from src.cart.models import Carts, CartItems
from src.user.models import CustomUser
from api.serializers import CustomUserSerializer
from urllib.parse import urlencode


class TestCart(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create_user(
            username="testuser1",
            email="ikhiphap@wa.fo",
            first_name="Arthur",
            last_name="Morgan",
            password="testpassword",
            phone="(600) 875-9897",
        )
        self.client.login(username="testuser1", password="testpassword")

        self.user2 = CustomUser.objects.create_user(
            username="testuser2",
            email="ti@gek.us",
            first_name="Austin",
            last_name="Brady",
            password="testpassword",
            phone="(415) 877-9520",
        )

        self.user1_serialized = CustomUserSerializer(self.user1).data
        self.cart1_data = {"created_by": "testuser1", "status": "Active"}

        self.cart1 = Carts.objects.create(created_by=self.user1, status="Active")
        self.cart2 = Carts.objects.create(created_by=self.user2, status="Active")

    # def test_cart_creation(self):
    #     cart_url = reverse("ecommerce_api:carts-list")
    #     response = self.client.post(cart_url, self.cart1_data, format="json")

    def test_cart_get_all_items(self):
        cart_url = reverse("ecommerce_api:carts-list")
        response = self.client.get(cart_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_cart_deletion(self):
    #     cart_url = reverse("ecommerce_api:carts-list")
    #     response = self.client.delete(cart_url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
