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
* python manage.py test src.clients.tests
* python manage.py test src.clients.tests.tests_clients_endpoints

Run all tests defined in this class:
* python manage.py test src.clients.tests.tests_clients_endpoints.ClientsTestCase

Run one specific test defined inside this class
* python manage.py test src.users.tests.tests_users_endpoints.UsersTestCase.test_user_register

"""

from django.test import TestCase
import requests
import os

from rest_framework import status


class ClientsTestCase(TestCase):
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
        pass

    # -----------------------------------------------------
    # remote/
    # -----------------------------------------------------
    def test_clients_remote_get(self):
        """
        Test register a user
        Endpoint: users/register/

        curl -d "username=user1&password=strong_pass1" http://localhost:9000/users/register/

        python manage.py test src.users.tests.tests_users_endpoints.UsersTestCase.test_user_register_existent

        :return:
        """
        # print('Testing =>', UsersTestCase.test_user_register_existent.__name__)
        # endpoint_user_register = self._host_test + self._endpoint_user_register
        # data = {'username': self._user_name, 'password': self._user_pass}
        # r = requests.post(endpoint_user_register, data=data).json()
        # result_exist = r.get('username')[0]
        # expected_str = 'A user with that username already exists.'
        # self.assertEqual(expected_str, result_exist)
        exp_str = 'OK'
        res_str = 'OK'
        self.assertEqual(exp_str, res_str)

    def test_clients_remote_post(self):
        """

        """
        exp_str = 'OK'
        res_str = 'OK'
        self.assertEqual(exp_str, res_str)

    # -----------------------------------------------------
    # commands/
    # -----------------------------------------------------
    def test_clients_commands_get(self):
        """

        """
        exp_str = 'OK'
        res_str = 'OK'
        self.assertEqual(exp_str, res_str)

    def test_clients_commands_post(self):
        """

        """
        exp_str = 'OK'
        res_str = 'OK'
        self.assertEqual(exp_str, res_str)

    # -----------------------------------------------------
    # command/
    # -----------------------------------------------------
    def test_clients_command_pk(self):
        """

        """
        exp_str = 'OK'
        res_str = 'OK'
        self.assertEqual(exp_str, res_str)

    # -----------------------------------------------------
    # config/
    # -----------------------------------------------------
    def test_clients_config_get(self):
        """

        """
        exp_str = 'OK'
        res_str = 'OK'
        self.assertEqual(exp_str, res_str)