#!/bin/bash

# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

# commands definitions
PYTHON_CMD='python3'

# folders names definitions
DEVELOPMENT_ENV_PATH='development_env'
COMMON_ENV_PATH='bin/activate'

# software folders names
ROOT_FOLDER_NAME='est_api_recipes'
REMOTE_CLIENT_GENERIC_NAME='remote_client_generic'


# project folders
ROOT_FOLDER_F=$HOME/$DEVELOPMENT_PATH/$ROOT_FOLDER_NAME/
REMOTE_CLIENT_GENERIC_F=$ROOT_FOLDER_F$REMOTE_CLIENT_GENERIC_NAME/


# environment folders
ENV_NAME='_venv'
ROOT_ENV_F=$HOME/$DEVELOPMENT_ENV_PATH/$ROOT_FOLDER_NAME$ENV_NAME/
REMOTE_CLIENT_GENERIC_ENV_F=$ROOT_ENV_F$REMOTE_CLIENT_GENERIC_NAME$ENV_NAME/

# creating environments automatically
$PYTHON_CMD -m venv $REMOTE_CLIENT_GENERIC_ENV_F
source $REMOTE_CLIENT_GENERIC_ENV_F$COMMON_ENV_PATH

python remote_client_main.py
deactivate
