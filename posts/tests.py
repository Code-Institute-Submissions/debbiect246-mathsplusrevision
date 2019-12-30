from django.test import TestCase

# Create your tests here.


class PostTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = title(name='Blog title')
        self.assertEqual(str(test_name), 'Blog title')
