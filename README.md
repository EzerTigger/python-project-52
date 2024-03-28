### Tests and linter status:
[![Actions Status](https://github.com/EzerTigger/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EzerTigger/python-project-52/actions)
[![test](https://github.com/yuriy-kormin/python-project-52/actions/workflows/django-test.yml/badge.svg)](https://github.com/EzerTigger/python-project-52/actions/workflows/django-test.yml)
[![lint](https://github.com/yuriy-kormin/python-project-52/actions/workflows/linter-run.yml/badge.svg)](https://github.com/EzerTigger/python-project-52/actions/workflows/linter-run.yml)
https://task-manager-bvfm.onrender.com


## Task Manager
A task management web application built with Python and Django framework. 
It allows you to set tasks, assign executors and change their statuses. 
Registration and authentication are required to work with the system.
***
## Getting Started

#### Clone the current repository via command:
```git clone https://github.com/EzerTigger/python-project-52``

***

## Requirements
* python >= 3.10
* Poetry >= 1.5.1
***

## Required packages

* Required packages are shown inside pyproject.toml

***

##  Environment variables

* DATABASE_URL
* SECRET_KEY
* ROLLBAR_ACCESS_TOKEN

Create `.env` file in the root folder and add these variables
***

## Makefile 

#### Current project starts after typing 2 commands :

* ``` make install```, which makes poetry install packages from pyproject.toml
* ```make migrate```, which create tables in the database

#### You can also run:

Tests:
```make test```

Linter (Flake8):
```make lint```

***

## Start

Start the Gunicorn Web-server by running:

```make start```

Or start in development mode using:

```make dev```