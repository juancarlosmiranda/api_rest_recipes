#!/bin/bash
# Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
# Date: June 2024
# Description:
#
# Use:
#

# commands definitions
PYTHON_CMD='python3'

# folders names definitions
DEVELOPMENT_PATH_ENV='development_env'
ENV_ACIVATE_CMD='bin/activate'

# software folders names
REPOSITORY_NAME='rest_api_recipes'
REST_API_SERVER_NAME='rest_api_server'


# environment folders
ENV_NAME='_venv'
REPOSITORY_PATH_ENV=$HOME/$DEVELOPMENT_PATH_ENV/$REPOSITORY_NAME$ENV_NAME/
REST_API_SERVER_PATH_ENV=$REPOSITORY_PATH_ENV$REST_API_SERVER_NAME$ENV_NAME/


source $REST_API_SERVER_PATH_ENV$ENV_ACIVATE_CMD
python manage.py runserver 0:9000

echo "-------------------------------------"
echo "Write deactivate"
echo "-------------------------------------"
deactivate
