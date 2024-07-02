#!/bin/bash
# Project: REST API RECIPES https://github.com/juancarlosmiranda/rest_api_recipes
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
# Date: June 2024
# Description:
# This script creates a hierarchy folder to save this project. Also, it install
# Python environment.

# Use:
# ./creating_env_server.sh
#
# Python environment hierarchy
#|__/development_env/
#   |__/rest_api_recipes_venv/
#   |   |__/rest_api_server-venv/
#
#
set -e
REQUERIMENTS_LINUX='requirements_linux.txt'

# commands definitions
MKDIR_CMD='mkdir -p '
CHMOD_CMD='chmod 755 '
SOURCE_CMD='source '
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
#REPOSITORY_PATH=$HOME/$DEVELOPMENT_PATH/$REPOSITORY_NAME/
#REST_API_SERVER_PATH=$REPOSITORY_PATH$REST_API_SERVER_NAME/

# environment folders
ENV_NAME='_venv'
REPOSITORY_PATH_ENV=$HOME/$DEVELOPMENT_PATH_ENV/$REPOSITORY_NAME$ENV_NAME/
REST_API_SERVER_PATH_ENV=$REPOSITORY_PATH_ENV$REST_API_SERVER_NAME$ENV_NAME/

# ----------------------------------------------
# Main
# ----------------------------------------------

if [ -d $DEVELOPMENT_PATH ]
then
echo "-------------------------------------"
  echo "Development path = "$DEVELOPMENT_PATH
echo "-------------------------------------"
else
echo "-------------------------------------"
  echo "Creating development path -> "
  echo "-------------------------------------"
  $MKDIR_CMD$DEVELOPMENT_PATH
fi

if [ -d $DEVELOPMENT_PATH_ENV ]
then
  echo "Development path environment = "$DEVELOPMENT_PATH_ENV
else
  echo "Creating development path environment -> "
  $MKDIR_CMD$DEVELOPMENT_PATH_ENV
fi

#if [ -d $REPOSITORY_PATH ]
#then
#  echo "Repository path = "$REPOSITORY_PATH
#else
#  echo "Creating repository path -> "
#  $MKDIR_CMD$REPOSITORY_PATH
#fi

#if [ -d $REST_API_SERVER_PATH ]
#then
#  echo "Repository REST API path = "$REST_API_SERVER_PATH
#else
#  echo "Repository REST API path -> "
#    $MKDIR_CMD$REPOSITORY_PATH
#  # mkdir
#fi

echo "-------------------------------------"
echo "Creating Python virtual environment"
echo "-------------------------------------"
echo "REPOSITORY_PATH="$REPOSITORY_PATH
echo "REST_API_SERVER_PATH_ENV = "$REST_API_SERVER_PATH_ENV
$PYTHON_CMD -m venv $REST_API_SERVER_PATH_ENV
$SOURCE_CMD$REST_API_SERVER_PATH_ENV$ENV_ACIVATE_CMD

echo "-------------------------------------"
echo "Updating / Installing requirements"
echo "-------------------------------------"
echo "requirements.txt = "$REST_API_SERVER_PATH$REQUERIMENTS_LINUX
$PIP_UPDATE_CMD
$PIP_INSTALL_CMD -r $REQUERIMENTS_LINUX
deactivate
echo "-------------------------------------"
echo "Activate the environment with:"
echo "-------------------------------------"
echo "run from the console for server starting ./rest_api_server.start.sh"
echo "or activate manually with:"
echo $SOURCE_CMD$REST_API_SERVER_PATH_ENV$ENV_ACIVATE_CMD

