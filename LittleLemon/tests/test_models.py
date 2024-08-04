from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id = 1,title="IceCream", price=80, inventory=50)
        self.assertEqual(str(item), "IceCream : 80")
    