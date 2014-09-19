Django17-template project
=========================

A `cookiecutter`_ template for Django17.

Version: 0.1

Features
--------

* Django 1.7
* Use `cookiecutter`_ to build new project
* django-environ (config/.env)
* django-braces
* django-model-utils
* django-extensions
* two-scoops like settings (package with `development.py`, `production.py` and `test.py`)
* django-debug-toolbar (only `development.py`)
* docs with Sphinx
* tests with Selenium and coverage

Usage
-----

To build new project:

.. code-block:: bash

    pip install cookiecutter
    cookiecutter https://github.com/openpolis/django16-template.git --checkout django17

    cd <repo_name>
    mkvirtualenv <repo_name>
    setvirtualenvproject
    pip install -r requirements/development.txt
    python project/manage.py syncdb
    python project/manage.py runserver

Edit `config/.env` with your setting values.

Other templates
---------------

- https://github.com/rdegges/django-skel
- https://github.com/jezdez/django-configurations/tree/templates/1.5.x
- https://github.com/jezdez/django-configurations/tree/templates/1.6.x
- https://github.com/twoscoops/django-twoscoops-project
- https://github.com/pydanny/cookiecutter-django

.. _cookiecutter: https://github.com/audreyr/cookiecutter


