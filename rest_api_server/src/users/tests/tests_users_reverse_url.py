"""
Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: June 2024
Description:

Use:
python manage.py test src.users.tests.tests_reverse_url
"""
from django.urls import reverse
from rest_framework.test import APITestCase

class URLTest(APITestCase):
    """
    Check src.users.urls.py to see views names
    """
    def setUp(self):
        self.protocol = 'http'
        self.server = 'localhost'
        self.port = '9000'
        self.host_to_test = self.protocol + '://' + self.server + ':' + self.port
        self.rest_api_endpoint = 'v1'
        self.module_root = 'users'
        self.endpoint_user_register = '/' + self.module_root + '/' + 'register' + '/'
        self.endpoint_user_login = '/' + self.module_root + '/' + 'login' + '/'
        self.endpoint_user_refresh = '/' + self.module_root + '/' + 'refresh' + '/'
        self.endpoint_user_logout = '/' + self.module_root + '/' + 'logout' + '/'

        pass
        # self.client = APIClient()

    def test_url_register_view(self):
        print(f'{URLTest.test_url_register_view.__name__} -> Testing reverse url {self.endpoint_user_register}')
        result_url = reverse('register_view')
        print(result_url)
        self.assertEqual(self.endpoint_user_register, result_url)

    def test_url_login_view(self):
        print(f'{URLTest.test_url_login_view.__name__} -> Testing reverse url {self.endpoint_user_login}')
        result_url = reverse('login_view')
        print(result_url)
        self.assertEqual(self.endpoint_user_login, result_url)

    def test_url_refresh_view(self):
        print(f'{URLTest.test_url_refresh_view.__name__} -> Testing reverse url {self.endpoint_user_refresh}')
        result_url = reverse('refresh_view')
        print(result_url)
        self.assertEqual(self.endpoint_user_refresh, result_url)

    def test_url_logout_view(self):
        print(f'{URLTest.test_url_logout_view.__name__} -> Testing reverse url {self.endpoint_user_logout}')
        result_url = reverse('logout_view')
        print(result_url)
        self.assertEqual(self.endpoint_user_logout, result_url)
