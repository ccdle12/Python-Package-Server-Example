# Python-Package-Server-Example
A reference example project for hosting a private python package server to share libraries

## Background

This project serves a private pypi server in a simple microserver environment. 

The services `project_a` and `project_b` rely on a package called `library_example` being served by the service `pypi_project`.

Some things to keep in mind...

* `project_a` and `project_b` both need to run `pip install library_example` in their containers. We are using a file `/root/.pip/pip.conf` to set a private pypi server.

* In order for `project_a` and `project_b` to install `library_example`, `pypi_project` needs to be running and serving before `project_a` and `project_b` become live.


## Getting Started

The following instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Dependencies you need to install the software.

* docker
* docker-compose


### Installing

Run the project

```
$ docker-compose up
```

## Running the tests

The tests will show that both `project_a` and `project_b` will return a message using the library from the private server.

```
$ ./test.sh

>
{
  "message": "project_b: this was called from the example library"
}
{
  "message": "project_a: this was called from the example library"
}
```

# How to set up a private package server
The following instructions explain how to create a pypi server. This is *NOT* needed to run this project.

#### 1. Create a project

Create a project folder structure like the following:

```
├── README.md
├── library_example
│   └── __init__.py
├── setup.cfg
└── setup.py
```

#### 2. Add library details to setup.py
Example of setup.py:

```
from setuptools import setup

setup(
    name='library_example',
    packages=['library_example'],
    description='Some Project to be shared',
    version='0.1',
    url='http://github.com/itc/library_example',
    author='Dev',
    author_email='docs@something.com',
    keywords=['pip','library','example']
    )
```

#### 3. An a class or function to _ _init_ _.py

```
def lib_example_call():
    return "this was called from the example library"
```

#### 4. Update setup.cfg
```
[metadata]
description-file = README.md
```

#### 5. Compress the python package for download

A dist folder will be created.

```
$ python setup.py sdist
```

#### 6. Install a pypi server

```
$ pip install pypiserver
```

#### 7. Serve the pypi server

This will serve the pypi server on localhost or whichever IP/machine it's deployed to on port 8080.
```
$ mv /dist/library_example-0.1.tar.gz /packages
$ pypi-server -p 8080 /packages
```

#### 8. Create pip.config on client machines and install library

Create a folder `.pip` at `/root/`.
```
$ mkdir /root/.pip
```

Create a file `pip.conf` in `.pip`.
```
$ touch /root/.pip/pip.conf
```

Add the following to `pip.conf`.
```
[global]
extra-index-url = http://<pypi-server-ip>:8080/
trusted-host = <pypi-server-ip>
```

Install the library
```
$ pip install library_example
```
