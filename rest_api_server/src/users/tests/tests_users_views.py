"""
Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: June 2024
Description:
This test class-views without a REST API server running

Usage
Run all tests.
* python manage.py test

Run all tests defined in file:
* python manage.py test src.users.tests
* python manage.py test src.users.tests.tests_users_views

Run all tests defined in this class:
* python manage.py test src.users.tests.tests_users_endpoints.UsersTestCaseViews

Run one specific test defined inside this class
* python manage.py test src.users.tests.tests_users_endpoints.UsersTestCaseViews.test_user_register_view

"""

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.test import TestCase

from src.users.views import UserRegisterView

class UsersTestCaseViews(TestCase):
    def setUp(self):
        print('UsersTestCaseViews.setUp()')
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="emailuser", email="email_user@mydomain.com", password="top_secret"
        )

    def test_user_register_view(self):
        """
        curl -d "username=user1&password=strong_pass1" http://localhost:9000/users/register/
        """
        print('test_user_register_view ->')
        requested_data = {
            'username': 'user109',
            'password': 'password'
        }
        request_to_view = self.factory.post('/users/register/', requested_data)
        request_to_view.user = AnonymousUser()

        response_from_view = UserRegisterView.as_view()(request_to_view)
        print(response_from_view)
        print(response_from_view.data)
        response_from_view_data_str = str(response_from_view.data)
        exp_response_data_str = "{'id': 2, 'username': 'user109'}"
        self.assertEqual(exp_response_data_str, response_from_view_data_str)
        pass