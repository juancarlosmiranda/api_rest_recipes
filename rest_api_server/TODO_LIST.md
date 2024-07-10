# TODO LIST

Add headers to every project's file.
Add test for models.
Add coverage test for endpoints
Add an automatic config for IP NUMBER in settings.py
Add HTTPS certificates.

Installing packages manually.
```
pip install asgiref certifi cffi chardet charset-normalizer cryptography Deprecated dj-database-url django django-cors-headers django-extensions django-filter django-oauth-toolkit django-rest-framework djangorestframework idna jwcrypto oauthlib pycparser pytz requests six sqlparse typing-extensions urllib3 whitenoise wrapt
```
one by one by command line.
```
pip install asgiref
pip install certifi
pip install cffi
pip install chardet
pip install charset-normalizer
pip install cryptography
pip install Deprecated
pip install dj-database-url
pip install django
pip install django-cors-headers
pip install django-extensions
pip install django-filter
pip install django-oauth-toolkit
pip install django-rest-framework
pip install djangorestframework
pip install idna
pip install jwcrypto
pip install oauthlib
pip install pycparser
pip install pytz
pip install pkg_resources
pip install requests
pip install six
pip install sqlparse
pip install typing-extensions
pip install urllib3
pip install whitenoise
pip install wrapt
```

A good installation example. https://fly.io/docs/flyctl/install/
Buen ejemplo de comando /home/usuario/.fly/bin/flyctl --help

## Testing in Django
[How to correct - Django testing views - getting error - DiscoverRunner.run_tests() takes 2 positional arguments but 3 were given](https://stackoverflow.com/questions/77227048/django-testing-views-getting-error-discoverrunner-run-tests-takes-2-positi)
To not downgrade to previous Django version, you can make small fix to your django package:
Example path:
some_path_to/virtualenv/lib/python3.11/site-packages/django/test/runner.py (probably at line 1044)
def run_tests(self, test_labels, some=None, **kwargs):
add any parameter like some=None


Test unitarios
-----------------

Test suite
Test de urls endpoints
Test de vistas
Test de serializers
Test de modelos / tablas
Test de APIS
Colocar datos de prueba y borrar la base de datos de prueba.


