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

#### Check your pip version with the following command:
```python -m pip --version```

#### Make sure that pip is always up-to-date. If not, use the following:
```python -m pip install --upgrade pip```

#### Next install poetry on your OS. (the link is below)
[Poetry installation](https://python-poetry.org/docs/)
##### don't forget to init poetry packages with command ```poetry init```

### 

*** 

## Makefile 

#### Current project starts after typing 2 commands :

* ``` make install```, which makes poetry install packages from pyproject.toml
* ```make lock```, which locks poetry packages inside poetry.lock
***

#### After configuration, you should use ```make dev``` to start your app