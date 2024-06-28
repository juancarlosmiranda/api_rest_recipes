# REST API RECIPES

## Table of Contents
- [Clone repository](#clone-repository)
- [Install and run](#install-and-run)
- [Create database settings](#create-database-settings)
- [Run server](#run-server)
- [Test connectivity](#test-connectivity)
- [Deploy service on Internet](#deploy-service-on-internet)



## Clone repository
From Linux systems, run this script at the command line to automatically create directory hierarchies for the project's development environments. Then use the "create_env_xxxxxx.sh" scripts for each component to load the Python dependencies.

Clone the repository with:
```
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


python3 -m venv ./rest_api_server-venv
source ./rest_api_server-venv/bin/activate
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
Change ocurrences in settings.py
ROOT_URLCONF = 'api_rest.urls'






rest api server
web ui interface
