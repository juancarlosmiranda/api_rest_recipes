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
    path('example1/', views.NotImplementedYet.as_view()),
    path('menu/', views.NotImplementedYet.as_view()),
    path('profile/<int:pk>/', views.UserData.as_view())
]
