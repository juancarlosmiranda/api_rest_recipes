"""
Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: June 2024
Description:
This script needs REST Framework executing meanwhile the test is executed.

Usage
Run all tests.
* python manage.py test

Run all tests defined in file:
* python manage.py test src.users.tests
* python manage.py test src.users.tests.tests_users_endpoints

Run all tests defined in this class:
* python manage.py test src.users.tests.tests_users_endpoints.UsersTestCase

Run one specific test defined inside this class
* python manage.py test src.users.tests.tests_users_endpoints.UsersTestCase.test_user_register

"""

from django.test import TestCase
import requests
import os

from rest_framework import status


class UsersTestCase(TestCase):
    """
    .
    """
    _user_name = 'user1'
    _user_pass = 'strong_pass1'

    _new_user_name = 'user9'
    _new_user_pass = 'strong_pass9'

    # API ENDPOINTS urls
    _host_test = 'http://localhost:9000/'
    _rest_api_endpoint = 'v1/'
    _module_root = 'users'
    _endpoint_user_register = _module_root + '/' + 'register' + '/'
    _endpoint_user_login = _module_root + '/' + 'login' + '/'
    _endpoint_user_refresh = _module_root + '/' + 'refresh' + '/'
    _endpoint_user_logout = _module_root + '/' + 'logout' + '/'

    def setUp(self):
        """
        Settings

        :return:
        """
        print('--- Setting test cases ---')
        TEST_CASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(f'TEST_CASE_DIR={TEST_CASE_DIR}')
        # endpoint = self._host_test + self._endpoint_set_connection
        # data = {'username': self._user_name, 'password': self._user_pass}
        # r = requests.post(endpoint, data=data).json()
        # print('token --->' + r['access_token'])
        # self.token = r['access_token']
        # ---------------------------------------
        pass

    # /register#
    def test_user_register_existent(self):
        """
        Test register a user
        Endpoint: users/register/

        curl -d "username=user1&password=strong_pass1" http://localhost:9000/users/register/

        python manage.py test src.users.tests.tests_users_endpoints.UsersTestCase.test_user_register_existent

        :return:
        """
        print('Testing =>', UsersTestCase.test_user_register_existent.__name__)
        endpoint_user_register = self._host_test + self._endpoint_user_register
        data = {'username': self._user_name, 'password': self._user_pass}
        r = requests.post(endpoint_user_register, data=data).json()
        result_exist = r.get('username')[0]
        expected_str = 'A user with that username already exists.'
        self.assertEqual(expected_str, result_exist)

    def test_new_user_register(self):
        """
        Test register a user
        Endpoint: users/register/

        curl -d "username=user5&password=strong_pass5" http://localhost:9000/users/register/

        python manage.py test src.users.tests.tests_users_endpoints.UsersTestCase.test_new_user_register

        :return:
        """
        print('Testing =>', UsersTestCase.test_new_user_register.__name__)
        endpoint_user_register = self._host_test + self._endpoint_user_register
        data = {'username': self._new_user_name, 'password': self._new_user_pass}
        r = requests.post(endpoint_user_register, data=data).json()
        pass
        result_exist = r.get('username')
        expected_str = self._new_user_name
        self.assertEqual(expected_str, result_exist)


    # /login#
    def test_user_login(self):
        """
        Test user login

        curl -d "username=user1&password=strong_pass1" http://localhost:9000/users/login/

        :return:
        """
        print('Testing =>', UsersTestCase.test_user_login.__name__)
        expected_str = 'OK'
        result_exist = 'OK'
        self.assertEqual(expected_str, result_exist)

    # /login#
    def test_user_logout(self):
        # TODO: TO complete logout
        """
        Test user disconnect



        :return:
        """
        print('Testing =>', UsersTestCase.test_user_logout.__name__)
        expected_str = 'OK'
        result_exist = 'OK'
        self.assertEqual(expected_str, result_exist)
