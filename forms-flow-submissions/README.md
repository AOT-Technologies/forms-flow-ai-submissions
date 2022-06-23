# Submission Reference API

[![FormsFlow API CI](https://github.com/AOT-Technologies/forms-flow-ai-dev/actions/workflows/forms-flow-api-ci.yml/badge.svg?branch=develop)](https://github.com/AOT-Technologies/forms-flow-ai-dev/actions)
![Python](https://img.shields.io/badge/python-3.9-blue) ![Flask](https://img.shields.io/badge/Flask-1.1.4-blue) ![postgres](https://img.shields.io/badge/postgres-11.0-blue)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

**formsflow.ai** has built this adaptive tier for correlating form management, BPM and analytics together.

The goal of the Submission Reference API is to provide access to all submitted data. It is built using Python :snake: .

## Table of Content

1. [Prerequisites](#prerequisites)
2. [Solution Setup](#solution-setup)
   * [Step 1 : Installation](#installation)
   * [Step 2 : Environment Configuration](#environment-configuration)
   * [Step 3 : Running the Application](#running-the-application)
   * [Step 4 : Verify the Application Status](#verify-the-application-status)


## Prerequisites

* For docker based installation [Docker](https://docker.com) need to be installed.
* Admin access to [Keycloak](../forms-flow-idm/keycloak) server and ensure audience(camunda-rest-api) is setup in Keycloak-bpm server.

## Solution Setup

### Installation

If you are interested in contributing to the project, you can install through docker or locally.

It's recommended to download dev-packages to follow Python coding standards for project like PEP8 if you are interested in contributing to project.
You installing dev-packages using pip as follows:

```python3 -m pip install -r requirements/dev.txt```

### Keycloak Setup

No specific client creation is required. Audience has been added for clients
**forms-flow-web** and **forms-flow-bpm**.  

### Environment Configuration

* Make sure you have a Docker machine up and running.
* Make sure your current working directory is "forms-flow-submissions".
* Rename the file [sample.env](./sample.env) to **.env**.
* Modify the environment variables in the newly created **.env** file if needed. Environment variables are given in the table below,
* **NOTE : {your-ip-address} given inside the .env file should be changed to your host system IP address. Please take special care to identify the correct IP address if your system has multiple network cards**

> :information_source: Variables with trailing :triangular_flag_on_post: in below table should be updated in the .env file

Variable name | Meaning | Possible values | Default value |
--- | --- | --- | ---
`INSIGHT_API_URL`:triangular_flag_on_post: | The forms-flow-analytics Api base end-point | | <http://{your-ip-address}:7000> |
`INSIGHT_API_KEY` :triangular_flag_on_post: | The forms-flow-analytics admin API key | | `Get the api key from forms-flow-analytics (REDASH) by following the 'Get the Redash API Key' steps from [here](../forms-flow-analytics/README.md#get-the-redash-api-key)`
`SUBMISSION_API_DB_USER`|formsflow database postgres user|Used on installation to create the database.Choose your own|`postgres`
`SUBMISSION_API_DB_PASSWORD`|formsflow database postgres password|Used on installation to create the database.Choose your own|`changeme`
`SUBMISSION_API_DB_NAME`|formsflow database name|Used on installation to create the database.Choose your own|`SUBMISSION_API_DB`
`SUBMISSION_API_DB_URL`|JDBC DB Connection URL for formsflow||`postgresql://postgres:changeme@forms-flow-submission-db:5432/submissionapi`
`KEYCLOAK_URL`:triangular_flag_on_post:| URL to your Keycloak server || `http://{your-ip-address}:8080`
`KEYCLOAK_URL_REALM`|The Keycloak realm to use|eg. forms-flow-ai | `forms-flow-ai`
`KEYCLOAK_BPM_CLIENT_ID`|Client ID for Camunda to register with Keycloak|eg. forms-flow-bpm|`forms-flow-bpm`
`KEYCLOAK_BPM_CLIENT_SECRET`|Client Secret of Camunda client in realm|eg. 22ce6557-6b86-4cf4-ac3b-42338c7b1ac12|`e4bdbd25-1467-4f7f-b993-bc4b1944c943` <br><br>`To generate a new keycloak client seceret by yourself follow the steps from` [here](../forms-flow-idm/keycloak/README.md#getting-the-client-secret)
`KEYCLOAK_WEB_CLIENT_ID`|Client ID for formsflow to register with Keycloak|eg. forms-flow-web|`forms-flow-web`
`CAMUNDA_API_URL`:triangular_flag_on_post:|Camunda Rest API URL||`http://{your-ip-address}:8000/camunda`
`SUBMISSION_API_URL`:triangular_flag_on_post:|formsflow.ai Rest API URL||`http://{your-ip-address}:6212`
`SUBMISSION_API_CORS_ORIGINS`| formsflow.ai Rest API allowed origins, for allowing multiple origins you can separate host address using a comma seperated string or use * to allow all origins |eg:`host1, host2, host3`| `*`

**NOTE : Default realm is `forms-flow-ai`**

### Running the Application

* forms-flow-submissions service uses port 6212, make sure the port is available.
* `cd {Your Directory}/forms-flow-submissions`

* Run `docker-compose up -d` to start.


*NOTE: Use --build command with the start command to reflect any future **.env** changes eg : `docker-compose up --build -d`*

#### To Stop the Application

* Run `docker-compose stop` to stop.


### Verify the Application Status

   The application should be up and available for use at port defaulted to 6212 in <http://localhost:6212/>
  
* Access the **/checkpoint** endpoint for a Health Check on API to see it's up and running.

```
GET http://localhost:6212/checkpoint

RESPONSE

{
    "message": "Welcome to formsflow.ai Submissions API"
}
```

* Get the access token

```
POST {Keycloak URL}/auth/realms/<realm>/protocol/openid-connect/token

Body:
grant_type: client_credentials
client_secret: {set client token}
client_id: forms-flow-bpm

Headers:
Content-Type : application/x-www-form-urlencoded

```
