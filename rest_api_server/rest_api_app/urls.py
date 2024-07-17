"""
Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: June 2024
Description:

Use:
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_api_app.settings import REST_API_ROOT

router = DefaultRouter()

urlpatterns = [
    # Oauth2 provider, it is like an external service
    path('admin/', admin.site.urls),  # admin web site interface
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # REST API SERVER
    path('rest_api_app/', include(router.urls)),
    path('users/', include('src.users.urls')),
    path('clients/', include('src.clients.urls')),
    #path(REST_API_ROOT, include('src.control_panel.urls')),
    #path(REST_API_ROOT, include('src.clients.urls')),

]
