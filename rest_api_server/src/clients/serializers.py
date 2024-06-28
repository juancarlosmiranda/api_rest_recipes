"""
Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: June 2024
Description:

Use:
"""

from rest_framework import serializers
from .models import RemoteClients
from .models import BroadcastMessages
from .models import BroadcastConfig

class RemoteClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteClients
        fields = '__all__'


class BroadcastMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroadcastMessages
        fields = '__all__'


class BroadcastConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroadcastConfig
        fields = '__all__'

