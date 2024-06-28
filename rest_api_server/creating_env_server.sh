#!/bin/bash
# Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
# Date: June 2024
# Description:
#
# Use:
#

set -e

#FILENAME_ZIP='ak_acquisition_system-main.zip'
REQUERIMENTS_LINUX='requirements_linux.txt'

# commands definitions

#UNZIP_CMD=`which unzip`
#MKDIR_CMD='mkdir -p'
#CHMOD_CMD='chmod 755'
PYTHON_CMD='python3'
PIP_INSTALL_CMD='pip install'
PIP_UPDATE_CMD='pip install --upgrade pip'

# files extensions names
#EXT_SCRIPTS_SH='*.sh'
#EXT_ZIP='.zip'

# folders names definitions
DEVELOPMENT_PATH='development'
DEVELOPMENT_PATH_ENV='development_env'
ENV_ACIVATE_CMD='bin/activate'


# software folders names
REPOSITORY_NAME='rest_api_recipes'
REST_API_SERVER_NAME='rest_api_server'


# project folders
REPOSITORY_PATH=$HOME/$DEVELOPMENT_PATH/$REPOSITORY_NAME/
REST_API_SERVER_PATH=$REPOSITORY_PATH$REST_API_SERVER_NAME/


# environment folders
ENV_NAME='_venv'
REPOSITORY_PATH_ENV=$HOME/$DEVELOPMENT_PATH_ENV/$REPOSITORY_NAME$ENV_NAME/
REST_API_SERVER_PATH_ENV=$REPOSITORY_PATH_ENV$REST_API_SERVER_NAME$ENV_NAME/

echo "-------------------------------------"
echo "Creating Python virtual environment"
echo "-------------------------------------"
echo "REPOSITORY_PATH="$REPOSITORY_PATH
echo "REST_API_SERVER_PATH_ENV = "$REST_API_SERVER_PATH_ENV

echo "-------------------------------------"
echo "Installing requirements"
echo "-------------------------------------"
echo "requirements.txt = "$REST_API_SERVER_PATH$REQUERIMENTS_LINUX

# creating environments automatically
$PYTHON_CMD -m venv $REST_API_SERVER_PATH_ENV
source $REST_API_SERVER_PATH_ENV$ENV_ACIVATE_CMD
$PIP_UPDATE_CMD
$PIP_INSTALL_CMD -r $REST_API_SERVER_PATH$REQUERIMENTS_LINUX
deactivate

