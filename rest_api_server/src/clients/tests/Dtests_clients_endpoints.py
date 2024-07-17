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
* python manage.py test src.clients.tests.tests_clients_endpoints.ClientsTestCaseEndpoints

Run one specific test defined inside this class
* python manage.py test src.clients.tests.tests_clients_endpoints.ClientsTestCaseEndpoints

"""

from django.test import TestCase
from rest_framework import status
import requests
import os



class ClientsTestCaseEndpoints(TestCase):
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
    _endpoint_set_connection = 'users/login/'
    _endpoint_end_connection = 'users/logout/'
    _module_root = 'clients'
    _endpoint_client_remote = _module_root + '/' + 'remote' + '/'
    _endpoint_client_commands = _module_root + '/' + 'commands' + '/'
    _endpoint_client_command = _module_root + '/' + 'command' + '/'
    _endpoint_client_config = _module_root + '/' + 'config' + '/'


    def setUp(self):
        """
        Settings, gets token for testing
        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"

        :return:
        """
        print('--- Setting test cases ---')
        TEST_CASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(f'TEST_CASE_DIR={TEST_CASE_DIR}')
        print('--- Setting test cases ---')
        endpoint = self._host_test + self._endpoint_set_connection
        data = {'username': self._user_name, 'password': self._user_pass}
        response_from_view = requests.post(endpoint, data=data).json()
        print('token --->' + response_from_view['access_token'])
        self.token = response_from_view['access_token']
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def tearDown(self) -> None:
        """
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"
        curl -X POST http://localhost:9000/users/logout/ -d "token=aFuNhKm2XfEO1VGIPHyx6x1qvqPPGR"
        """
        print('--- Unsetting test cases ---')
        print('token --->' + self.token)
        endpoint = self._host_test + self._endpoint_end_connection
        data = {'token': self.token}
        response_from_view = requests.post(endpoint, data=data)
        print(response_from_view)
        pass
    # -----------------------------------------------------
    # remote/
    # -----------------------------------------------------
    def test_clients_remote_get(self):
        """
        Test get remote clients
        Endpoint: clients/remote/
        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X GET http://localhost:9000/client/remote/ -H "Authorization: Bearer A_TOKEN_HERE"
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"

        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X GET http://localhost:9000/clients/remote/ -H "Authorization: Bearer WYVXamVN2fPPb1BOLhGnM4X7aGoK0n"
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"

        :return:
        """
        print('Testing =>', ClientsTestCaseEndpoints.test_clients_remote_get.__name__)
        endpoint_client_get = self._host_test + self._endpoint_client_remote
        response_from_view = requests.get(endpoint_client_get, headers=self.headers)

        self.assertEqual(
            response_from_view.status_code,
            status.HTTP_200_OK, 'Status code, not equal to 200' + str(response_from_view)
        )

    def test_clients_remote_post_new(self):
        """
        Test create a new remote client
        Endpoint: clients/remote/

        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X POST http://localhost:9000/clients/remote/ -H "Authorization: Bearer A_TOKEN_HERE" -d "uuid=IIUUII&hostname=UNOHOST&os='WINDOWS'&ip='192.168.0.1'"
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"

        """
        print('Testing =>', ClientsTestCaseEndpoints.test_clients_remote_post_new.__name__)
        # "uuid=IIUUII&hostname=UNOHOST&os='WINDOWS'&ip='192.168.0.1'"
        data = {
            'uuid': 'IIUUII',
            'hostname': 'UNOHOST',
            'os': 'WINDOWS',
            'ip': '192.168.0.1'
        }

        endpoint_client_post = self._host_test + self._endpoint_client_remote
        response_from_view = requests.post(endpoint_client_post, headers=self.headers, data=data)

        exp_response_str = '{"status":201,"data":[{"pk":1}]}'  # new client
        self.assertEqual(exp_response_str, response_from_view.text, 'data is not equal')
        self.assertEqual(
            response_from_view.status_code,
            status.HTTP_201_CREATED, 'Status code, not equal to 201' + str(response_from_view.status_code)
        )

    def test_clients_remote_post_exist(self):
        """
        Test try to create a new remote clients, but it already exists
        Endpoint: clients/remote/

        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X POST http://localhost:9000/clients/remote/ -H "Authorization: Bearer A_TOKEN_HERE" -d "uuid=IIUUII&hostname=UNOHOST&os='WINDOWS'&ip='192.168.0.1'"
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"

        """
        print('Testing =>', ClientsTestCaseEndpoints.test_clients_remote_post_new.__name__)
        # "uuid=IIUUII&hostname=UNOHOST&os='WINDOWS'&ip='192.168.0.1'"
        data = {
            'uuid': 'IIUUII',
            'hostname': 'UNOHOST',
            'os': 'WINDOWS',
            'ip': '192.168.0.1'
        }
        endpoint_client_post = self._host_test + self._endpoint_client_remote
        response_from_view = requests.post(endpoint_client_post, headers=self.headers, data=data)
        # '{"status":200,"data":[{"pk":1,"hostname":"UNOHOST"}]}' # client exists
        exp_response_str = '{"status":200,"data":[{"pk":1,"hostname":"UNOHOST"}]}'
        self.assertEqual(exp_response_str, response_from_view.text, 'data is not equal')
        self.assertEqual(
            response_from_view.status_code,
            status.HTTP_200_OK, 'Status code, not equal to 200' + str(response_from_view.status_code)
        )


    # # -----------------------------------------------------
    # # commands/
    # # -----------------------------------------------------
    def test_clients_commands_get(self):
        """
        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X POST http://localhost:9000/clients/commands/ -H "Authorization: Bearer A_TOKEN_HERE"
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"

        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X GET http://localhost:9000/clients/commands/ -H "Authorization: Bearer 4zEmnVah8fsUVB8VH0oybZTjfr3gtl"
        curl -X POST http://localhost:9000/users/logout/ -d "4zEmnVah8fsUVB8VH0oybZTjfr3gtl"
        """

        print('Testing =>', ClientsTestCaseEndpoints.test_clients_commands_get.__name__)
        endpoint_client_commands_get = self._host_test + self._endpoint_client_commands
        response_from_view = requests.get(endpoint_client_commands_get, headers=self.headers)

        # {"id":1,"command":"WAITING","created":"2021-08-01T15:00:00Z"} if there are registers
        exp_response_str = '{"id":1,"command":"WAITING","created":"2021-08-01T15:00:00Z"}'
        self.assertEqual(exp_response_str, response_from_view.text, 'data is not equal')

        self.assertEqual(
            response_from_view.status_code,
            status.HTTP_200_OK, 'Status code, not equal to 200' + str(response_from_view)
        )

    def test_clients_commands_post(self):
        """
        Test creates new commands
        Endpoint: clients/commands/

        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X POST http://localhost:9000/clients/commands/ -H "Authorization: Bearer A_TOKEN_HERE" -d "command=START_RECORD"
        curl -X POST http://localhost:9000/clients/commands/ -H "Authorization: Bearer A_TOKEN_HERE" -d "command=STOP_RECORD"
        curl -X POST http://localhost:9000/clients/commands/ -H "Authorization: Bearer A_TOKEN_HERE" -d "command=WAITING"
        curl -X POST http://localhost:9000/clients/commands/ -H "Authorization: Bearer A_TOKEN_HERE" -d "command=STOP_REMOTE_CLIENT"
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"
        """
        print('Testing =>', ClientsTestCaseEndpoints.test_clients_commands_post.__name__)
        # "command=START_RECORD"
        data = {
            'command': 'WAITING',
        }
        endpoint_client_post = self._host_test + self._endpoint_client_commands
        response_from_view = requests.post(endpoint_client_post, headers=self.headers, data=data)
        # '{"status":201,"data":[{"pk":2}]}'
        exp_response_str = '{"status":201,"data":[{"pk":2}]}'
        self.assertEqual(exp_response_str, response_from_view.text, 'data is not equal')
        self.assertEqual(
            response_from_view.status_code,
            status.HTTP_201_CREATED, 'Status code, not equal to 201' + str(response_from_view.status_code)
        )


    # -----------------------------------------------------
    # config/
    # -----------------------------------------------------
    def test_clients_config_get(self):
        """
        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X GET http://localhost:9000/clients/config/ -H "Authorization: Bearer A_TOKEN_HERE"
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"
        """

        print('Testing =>', ClientsTestCaseEndpoints.test_clients_config_get.__name__)
        endpoint_client_config_get = self._host_test + self._endpoint_client_config
        response_from_view = requests.get(endpoint_client_config_get, headers=self.headers)

        exp_response_str = '{"id":1,"command":"WAITING","created":"2021-08-01T15:00:00Z"}'
        self.assertEqual(exp_response_str, response_from_view.text, 'data is not equal')

        self.assertEqual(
            response_from_view.status_code,
            status.HTTP_200_OK, 'Status code, not equal to 200' + str(response_from_view)
        )

    def test_clients_config_post(self):
        """
        curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
        curl -X POST http://localhost:9000/clients/config/ -H "Authorization: Bearer A_TOKEN_HERE" -d "sleep_time=5"
        curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"
        """
        print('Testing =>', ClientsTestCaseEndpoints.test_clients_config_post.__name__)
        # "sleep_time=5"
        data = {
            'sleep_time': '5',
        }
        endpoint_client_config_post = self._host_test + self._endpoint_client_config
        response_from_view = requests.post(endpoint_client_config_post, headers=self.headers, data=data)
        # '{"status":201,"data":[{"pk":2}]}'
        exp_response_str = '{"status":201,"data":[{"pk":2}]}'
        self.assertEqual(exp_response_str, response_from_view.text, 'data is not equal')
        self.assertEqual(
            response_from_view.status_code,
            status.HTTP_201_CREATED, 'Status code, not equal to 201' + str(response_from_view.status_code)
        )
        pass

    # # -----------------------------------------------------
    # # command/
    # # -----------------------------------------------------
    # def test_clients_command_pk(self):
    #     """
    #
    #     """
    #     exp_str = 'OK'
    #     res_str = 'OK'
    #     self.assertEqual(exp_str, res_str)
    #