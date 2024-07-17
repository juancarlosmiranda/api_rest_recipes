# REST API RECIPES

## Table of Contents
- [Clone repository](#clone-repository)
- [Install and run](#install-and-run)
- [Create database settings](#create-database-settings)
- [Run server](#run-server)
- [Test connectivity](#test-connectivity)
- [Deploy service on Internet](#deploy-service-on-internet)

**TODO LIST**
* ~~Deploy in Ubuntu Linux Server~~
* Deploy using a Docker file (create, update contents, deploy, test deploy)
* Deploy on External provider


## Clone repository
From Linux systems, run this script at the command line to automatically create directory hierarchies for the project's development environments. Then use the "create_env_xxxxxx.sh" scripts for each component to load the Python dependencies.

Clone the repository with:
```
mkdir development
cd development
git clone https://github.com/juancarlosmiranda/rest_api_recipes.git
```

## Install and run
In Linux systems execute as follows:
```
# Project's hierarchy
|__/development/
   |__/rest_api_recipes/
   |   |__/rest_api_server/
   |   |    |__/docs/
   |   |    |__/rest_api_app/
   |   |    |__/scripts/   
   |   |    |__/src/
   
   |__/WEB_UI/
   |   |__/TO_COMPLETE/
   |   |    |__/TO_COMPLETE/
   |   |        |__/TO_COMPLETE/
   |   |        |    |__/TO_COMPLETE/
   |   |        |       |__/TO_COMPLETE/

# Python environment hierarchy
|__/development_env/
   |__/rest_api_recipes_venv/
   |   |__/rest_api_server-venv/

```

Install packages on Linux systems.
```
sudo apt-get install python3-dev
sudo apt-get install python3
sudo apt-get install python3-pip
```


Create and activate environment.
```
[OPTIONAL]
mkdir rest_api_recipes_venv
cd rest_api_recipes_venv/


python3 -m venv ./rest_api_server_venv
source ./rest_api_server_venv/bin/activate
pip install --upgrade pip
```


#TODO: DJANGO REFERENCE add file description
```
python manage.py
```


## Create database settings
ss

## Run server
ff


## Test connectivity
dd

## Deploy service on Internet

To start the server you must follow the steps below:

    Install and run.
    Create database settings.
    Start server
    Test connectivity.

1. Install and run

In Linux systems execute as follows:

Create and activate environment.



# Change in app name
Change occurrences in settings.py
ROOT_URLCONF = 'api_rest.urls'


rest api server
web ui interface

# TODO WORKING NOW
# Deploy in Ubuntu Linux Server
This section is based on the minimal Ubuntu Server 22.04 image (ubuntu-24.04-live-server-amd64.iso) from [Get Ubuntu Server](https://ubuntu.com/download/server).
And it is about how to implement the REST API SERVER on a Linux image.
This section assumes that you have a virtual machine or a basic machine with Ubuntu Server installed.
In my case, I made this tutorial using a VirtualBox machine.


## Download the installation script.
```
wget https://raw.githubusercontent.com/juancarlosmiranda/rest_api_recipes/main/rest_api_server/install_ubuntu_minimal_22.04.sh; chmod 755 install_ubuntu_minimal_22.04.sh
```
Or by curl command.
```
curl -L https://raw.githubusercontent.com/juancarlosmiranda/rest_api_recipes/main/rest_api_server/install_ubuntu_minimal_22.04.sh | bash
```

Provides and environment with libraries and minimal requirements.
```
./install_ubuntu_minimal_22.04.sh
```

## Clone repository
From Linux systems, run this script at the command line to automatically create directory hierarchies for the project's development environments. Then use the "create_env_xxxxxx.sh" scripts for each component to load the Python dependencies.

Clone the repository with:
```
mkdir development
cd development
git clone https://github.com/juancarlosmiranda/rest_api_recipes.git
```
## Install and Run
Creates Python environment
```
cd rest_api_recipes
cd rest_api_server
./creating_env_server.sh
```
Run server
```
./rest_api_server_start.sh
```

## Django management cheatsheet
Create a project.
```
python3 -m django startproject api
django-admin startproject api
```

Create migrations files
```
python manage.py makemigrations
```
Migrates database changes
```
python manage.py migrate
```

Create a superuser
```
python manage.py createsuperuser
```
admin, admin@mydomain.com, admin12345
