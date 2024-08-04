from rest_framework import status
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title='Chocolate Cake', price=15.50)
        Menu.objects.create(title='Pancakes', price=5.50)

    def test_getall(self):
        url = 'http://localhost:8000/restaurant/menu/'
        response = self.client.get(url)
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)       