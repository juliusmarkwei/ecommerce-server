# testing users CRUD
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from src.user.models import CustomUser


class TestUser(APITestCase):
    endpoint = "/api/users/"
    client = APIClient()
    
    url = reverse("ecommerce_api:users")
    
    def test_user_creation(self):
        data = {
            "username": "testuser1",
            "first_name": "Corey",
            "last_name": "Lola",
            "email": "ajcah@kacudat.hr",
            "password": "testpass123",
            "phone": "(763) 491-6091",
        }
        
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                
    
    def test_get_user(self):
        #since the database doen't have any users for now
        # we need to create a user to be able to fetch by ID and Username
        
        testuser1 = CustomUser.objects.create_user(
            username="testuser1",
            password="test123",
            first_name="Dora",
            last_name="Maldonado",
            email="mecjeiz@zoh.hr",
            phone="(312) 515-6977",
        )
        
        testuser2 = CustomUser.objects.create_user(
            username="testuser2",
            password="test123",
            first_name="Austin",
            last_name="Bush",
            email="puderu@wo.me",
            phone="(542) 708-9526",
        )
        
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        
        
        response = self.client.get(self.url, kwargs={"id": 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        
        response = self.client.get(self.url, kwargs={"username": testuser2.username})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        
        
    def test_delete_user(self):
        
        testuser1 = CustomUser.objects.create_user(
            username="testuser1",
            password="test123",
            first_name="Austin",
            last_name="Bush",
            email="puderu@wo.me",
            phone="(542) 708-9526",
        )
        
        testuser2 = CustomUser.objects.create_user(
            username="testuser2",
            password="test123",
            first_name="Alejandro",
            last_name="Park",
            email="puakiwu@vavu.af",
            phone="(303) 470-1899",
        )
        
        response = self.client.delete(self.url, kwargs={"username", testuser2.username})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data["message"], "User deleted successfully")
        print(response.data["message"])