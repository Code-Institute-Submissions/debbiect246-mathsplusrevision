from .models import Product
from django.test import TestCase

# Create your tests here.


class ProductTests(TestCase):
    """
    Product model tests are shown below.
    To run them use python manage.py test Product
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
