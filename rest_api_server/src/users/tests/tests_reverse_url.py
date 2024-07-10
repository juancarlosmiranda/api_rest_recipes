from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase

"""
python manage.py test src.users.tests.test_reverse_url

"""


class URLTest(APITestCase):
    def setUp(self):
        pass
        # self.client = APIClient()

    def test_url_endpoint(self):
        print('nothing')
        url = reverse('register_view')
        print(url)
        pass
        expected_str = 'OK'
        result_exist = 'OK'
        self.assertEqual(expected_str, result_exist)
