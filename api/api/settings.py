"""
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(f'BASE_DIR={BASE_DIR}')

DEBUG = True

# Data connection, configure here all params
THIS_SERVER_IP = '192.168.0.103'
SERVER_IP = 'http://0.0.0.0'
SERVER_PORT = ':9000'
REST_API_SERVICE_URL = SERVER_IP + SERVER_PORT
REST_API_ROOT = 'v1/'  # Change the version of REST API here
ROOT_URLCONF = 'rest_api_app.urls'
STATIC_URL = '/static/'
WSGI_CONF = 'rest_api_app.wsgi.application'
# -----------------------
# In Linux use $ echo "a_password_to_set" | sha256sum
SECRET_KEY = 'django-insecure-oj)qp4-%=j6((p86t*som^)+x78^-=d(wqxi79^v5@c-xud+(j'
# Configuration of secret keys
# ---
# If you want change the secret keys values, you must change in /src/initial_data_values/oauth2_provider.json in fields:
# client_id and client_secret
CLIENT_IDENTIFIER_STR = 'super_secret_key_id.0#'
CLIENT_SECRET = 'super_secret_client_1234567891011121314151617181920.*#super_secret_client_1234567891011121314151617181920.*#'

# configure here IP
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', THIS_SERVER_IP, 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',  # Oauth2 provider
    'rest_framework',
    'src.users',  # application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',   # This should be first
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',  # Oauth2 provider
]

# Setup DRF to use Oauth2
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# --- Specify the authentication backends

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # To keep the Browsable API
    'oauth2_provider.backends.OAuth2Backend',
)

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'broadcast.db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
