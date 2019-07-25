# Python-Package-Server-Example
A reference example project for hosting a private python package server to share libraries

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Dependencies you need to install the software.
```
* docker
* docker-compose
```

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
