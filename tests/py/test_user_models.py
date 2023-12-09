# testing users CRUD
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from src.user.models import CustomUser
from urllib.parse import urlencode



class TestUser(APITestCase):
    endpoint = "/api/users/"
    client = APIClient()
    
    url = reverse("ecommerce_api:users-view")
    
    def test_user_creation(self):
        dummyUser = CustomUser.objects.create_user(
            username="dummyuser1",
            password="dummypass123",
            first_name="dummy",
            last_name="dummy",
            email="dummy@gmail.com",
            phone="000000000",
        )
        dummyUser.is_active = True
        self.client.login(username=dummyUser.username, password="dummypass123")
        
        data = {
            "username": "testuser1",
            "first_name": "Corey",
            "last_name": "Lola",
            "email": "ajcah@kacudat.hr",
            "password": "testpass123",
            "phone": "+076304916091",
        }
        
        response = self.client.post(self.url, data, format="json")
        self.client.logout()
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
        
        testuser1.is_active = True
        self.client.login(username=testuser1.username, password="test123")
        response = self.client.get(self.url, kwargs={"username": testuser1.username})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        
        response = self.client.get(self.url, kwargs={"id": 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.get(self.url, kwargs={"username": testuser2.username})
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
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
        
        testuser1.is_active = True
        self.client.login(username=testuser1.username, password="test123")
        response = self.client.delete(self.url + "?" + urlencode({"username": testuser2.username}), format=None)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data["message"], "User deleted successfully")
        self.client.logout()
        