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
    path('register/', views.UserRegister.as_view()),
    path('login/', views.token),
    path('login/refresh/', views.refresh_token),
    path('logout/', views.logout_token),
]
