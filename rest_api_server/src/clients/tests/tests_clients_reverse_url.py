"""
Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: June 2024
Description:

Use:
python manage.py test src.clients.tests.tests_clients_reverse_url
"""
from django.urls import reverse
from rest_framework.test import APITestCase

class UrlClientsTests(APITestCase):
    """
    Check src.clients.urls.py to see views names
    """
    def setUp(self):
        # API ENDPOINTS urls
        self.module_root = 'clients'
        self.endpoint_client_remote = '/' + self.module_root + '/' + 'remote' + '/'
        self.endpoint_client_commands = '/' + self.module_root + '/' + 'commands' + '/'
        self.endpoint_client_config = '/' + self.module_root + '/' + 'config' + '/'
        self.endpoint_client_command = '/' + self.module_root + '/' + 'command' + '/' + '1/'
        pass

    def test_url_remote_clients_view(self):
        print(f'{UrlClientsTests.test_url_remote_clients_view.__name__} -> Testing reverse url {self.endpoint_client_remote}')
        result_url = reverse('remote_clients_view')
        print(result_url)
        self.assertEqual(self.endpoint_client_remote, result_url)

    def test_url_command_broadcast_view(self):
        print(f'{UrlClientsTests.test_url_command_broadcast_view.__name__} -> Testing reverse url {self.endpoint_client_commands}')
        result_url = reverse('command_broadcast_view')
        print(result_url)
        self.assertEqual(self.endpoint_client_commands, result_url)

    def test_url_config_remote_clients_view(self):
        print(f'{UrlClientsTests.test_url_config_remote_clients_view.__name__} -> Testing reverse url {self.endpoint_client_config}')
        result_url = reverse('config_remote_clients_view')
        print(result_url)
        self.assertEqual(self.endpoint_client_config, result_url)

    def test_url_command_by_client_view(self):
        print(f'{UrlClientsTests.test_url_command_by_client_view.__name__} -> Testing reverse url {self.endpoint_client_command}')
        pk = 1
        result_url = reverse('command_by_client_view',args=[pk])
        print(result_url)
        self.assertEqual(self.endpoint_client_command, result_url)