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
    path('register/', views.UserRegisterView.as_view()),
    path('login/', views.SessionLoginView.as_view()),
    path('refresh/', views.SessionRefreshView.as_view()),
    path('logout/', views.SessionLogoutView.as_view()),
]
