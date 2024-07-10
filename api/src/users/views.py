"""
Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: June 2024
Description:

Use:
"""

import requests
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import CreateUserSerializer
from api.settings import REST_API_SERVICE_URL, CLIENT_IDENTIFIER_STR, CLIENT_SECRET




class UserRegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # it sends to an internal oauth2 server in /api
            r = requests.post('http://127.0.0.1:9000/o/token/',
                              data={
                                  'grant_type': 'password',
                                  'username': request.data['username'],
                                  'password': request.data['password'],
                                  'client_id': CLIENT_IDENTIFIER_STR,
                                  'client_secret': CLIENT_SECRET,
                              },
                              )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        print(f'LOGIN/ request={request}')
        print('user:', request.user)
        print('request.META:', request.META)
        print('request.META[PATH_INFO]:', request.META['PATH_INFO'])

        r = requests.post(REST_API_SERVICE_URL + '/o/token/',
                          data={
                              'grant_type': 'password',
                              'username': request.data['username'],
                              'password': request.data['password'],
                              'client_id': CLIENT_IDENTIFIER_STR,
                              'client_secret': CLIENT_SECRET,
                          },
                          )

        content = {
            'status': status.HTTP_200_OK,
            'data': 'EXAMPLE_POST'
        }
        print(f'From Oauth2 server={r.json()}')

        return Response(r.json())


class SessionRefreshView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # refresh
        print(f' REFRESH/ request={request}')
        #print('user:', request.user)
        print('request.META:', request.META)
        print('request.META[PATH_INFO]:', request.META['PATH_INFO'])
        print('request.data[refresh_token]', request.data['refresh_token'])

        r = requests.post(REST_API_SERVICE_URL + '/o/token/',
                          data={
                              'grant_type': 'refresh_token',
                              'refresh_token': request.data['refresh_token'],
                              'client_id': CLIENT_IDENTIFIER_STR,
                              'client_secret': CLIENT_SECRET,
                          },
                          )
        return Response(r.json())


class SessionLogoutView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        print(f' LOGOUT/ request={request}')
        #print('user:', request.user)
        print('request.META:', request.META)
        print('request.META[PATH_INFO]:', request.META['PATH_INFO'])

        r = requests.post(REST_API_SERVICE_URL + '/o/revoke_token/',
                          data={'token': request.data['token'],
                                'client_id': CLIENT_IDENTIFIER_STR,
                                'client_secret': CLIENT_SECRET,
                                },
                          )
        if r.status_code == requests.codes.ok:
            return Response({'message': 'token revoked'}, r.status_code)
        return Response(r.json(), r.status_code)
