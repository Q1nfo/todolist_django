<h1 align="center">Todolist on django by Q1nfo</h1>



**Source Code**: [github.com/q1nfo/todolist_django](https://github.com/Q1nfo/todolist_django/)

---

<!--intro-start-->
Todolist-django is a good example of creating a todolist in Django,
where all the necessary functionality is expressed in order to manage your time, create tasks,
as well as with the ability to share your plans with others.
In addition, this project presents a synchronous telegram bot integrated into Django that can help with managing your time and complementing the main functionality of the site.

To get started, jump to the [installation](#installation) section or keep reading to learn more about the included
features.
<!--intro-end-->

<!--readme-start-->

## ✨ Features

### 📦️ Django technologies

* [Django 4.2](https://www.djangoproject.com/) - Latest version of Django
* [DRF](https://www.django-rest-framework.org/) - is a powerful and flexible toolkit for building Web APIs
* [Poetry](https://python-poetry.org/) - Poetry comes with an exhaustive dependency resolver, which will always find a solution if it exists.
* [Django-Filter](https://django-filter.readthedocs.io/) - Django-filter is a generic, reusable application to alleviate writing some of the more mundane bits of view code.
* [Django-social-auth](https://github.com/python-social-auth/social-app-django) - Python Social Auth is an easy to setup social authentication/registration mechanism with support for several frameworks and auth providers.
* [Postgresql](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database
### 🩺 Code Quality, Formatting, and Linting Tools

* [Flake8](https://flake8.pycqa.org/) - Tool For Style Guide Enforcement
* [pre-commit](https://pre-commit.com/) - Git hook scripts are useful for identifying simple issues before submission to code review.
* [isort](https://pycqa.github.io/isort/) - isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.

## Installation

### Requirements

Before proceeding make sure you have installed [Docker](https://docs.docker.com/engine/installation/) . Docker with Docker Compose is used for local development.

### Manual Installation

    $ gh repo clone Q1nfo/todolist_django
    $ mv todolist_django example
    $ cd example

    touch .env && touch .env.db

    pip install poetry
    poetry init
    poetry install --no-ansi

### Apps

* GOALS -
This application implements the main functionality of creating management and sharing goals, categories for them and boards.

The user has the following options:

    -- Create a board
    -- Share a board with another user giving him Editor or Reader rights
    -- Create categories inside the board and manage them
    -- Create goals by giving them a deadline, category and urgency status

* BOT - A synchronous bot written as an application inside Django

The bot has the following options:

    -- Synchronize telegram profile and account on the website
    -- Create a goal in a specific category
    -- View all your goals

* CORE - Application responsible for creating and managing a user account

The core has the following options:

    -- Creating a user through the normal interface
    -- Creating a user via network protection
    -- Ability to view and edit profile
    -- Ability to change password

<!--readme-end-->
