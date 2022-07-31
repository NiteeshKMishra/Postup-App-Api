# Introduction

Goal of this project is to create apis for a social networking platform called PostUp.
This project is created with python django framework and postgres as database using Test driven development.

# Usage

This project is setup based on docker. So no need to create any virtualenv manually.
Everything is handled via docker from setting up virtualenv to installing dependencies
and running django commands.
Github actions are configured to run tests and linting on each push.

# PostUp

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/NiteeshKMishra/Postup-App-Api.git
    $ cd Postup-App-Api

Make sure you have support to run Makefile commands
[Setup support for Makefile](https://tldp.org/HOWTO/Software-Building-HOWTO-3.html)

Activate virtualenv and Install dependencies:

    $ make build

Apply the migrations:

    $ make migrate

Run the development server:

    $ make run

Stop development server:

    $ make down

## Available commands

Running tests:

    $ make test

Running linting:

    $ make lint

Creating a new app in project:

    $ make createapp app={{appName}}

Making new migrations:

    $ make makemigrations

Creating Django admin:

    $ make createadmin

## Api docs & Django Admin

Api docs can be accessed on route `/api/docs/`

Api schema can be accessed on route `/api/schema/`

Django admin can be accessed on route `/admin/`

