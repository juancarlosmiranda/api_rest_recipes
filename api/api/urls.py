"""

"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),  # admin web site interface
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # Oauth2 provider, it is like an external service
    path('user/', include('src.users.urls')),
]
