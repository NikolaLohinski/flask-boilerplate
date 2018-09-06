# Timeline-Inventions Challenge

- **Author** : [Nikola Lohinski](http://github.com/NikolaLohinski)
- **Date**: 02/09/2018

## Introduction

This is a small project that combines several containerized services through [Docker-compose](https://docs.docker.com/compose/overview/) :
- a [Flask](http://flask.pocoo.org/) REST API to make requests and query a database
- a [PostgreSQL](https://www.postgresql.org/) database to persist and organize data
- a front-end web application to interact with the API built with [VueJS](https://vuejs.org/) and served through [Webpack-dev-server](https://github.com/webpack/webpack-dev-server) for development purposes only

The goal is to build a simple web app based on a card/board game [Timeline-Inventions](https://www.boardgamegeek.com/boardgame/85256/timeline-inventions).

## Installation

To be able to build and serve the project, please follow official instructions and install [Docker](https://docs.docker.com/install/) and [Docker-compose](https://docs.docker.com/compose/install/#install-compose).

## Setup

Before mounting and running anything, you need to create a few environment variables. This can be done easily by creating a `.env` file next to the `docker-compose.yml` file, that will be picked up during the building process. You need to define :
- `POSTGRES_USER` : user name for postgres
- `POSTGRES_PASSWORD` : password for postgres
- `POSTGRES_DB` : name of the postgres database

## Usage

If you managed to complete the installation and setup properly, the simply run :
```
# -d is for detached mode
docker-compose up -d
```
Then you may visit :
- [http://localhost:8080/](http://localhost:8080/) with a web browser to see the front-end up and running
- [http://localhost:5000/](http://localhost:5000/) with [POSTMAN](https://www.getpostman.com/) (or simply a web browser) to query the API. For example, to get all inventions in the database :
  ```
    GET | http://localhost:5000/api/v0/inventions
  ```
NOTE: if you are running on Mac or Windows, you may need to replace `localhost` with the ip address of the container, which you may retrieve by inspecting the running container : `docker inspect <CONTAINER_ID or CONTAINER_NAME>` (Use `docker ps` to get information on the running containers)
