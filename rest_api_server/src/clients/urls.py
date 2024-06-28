"""
Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: June 2024
Description:

Use:
"""

from django.urls import path

from . import views

urlpatterns = [
    path('remote/', views.RemoteClientsViewSet.as_view()),
    path('commands/', views.CommandBroadcastList.as_view()),
    path('command/<int:pk>/', views.CommandByClient.as_view()),
    path('config/', views.ConfigRemoteClientsBroadcast.as_view())
]


