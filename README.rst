Django-project-template
=======================

A `cookiecutter`_ template for Django.

Version: 0.1

Features
--------

* Python 2.7, 3.4 or 3.5
* Django 1.9
* Django 1.10 ready (deprecations removed)
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
    cookiecutter https://github.com/openpolis/django-project-template.git
    # use option --checkout for specific branch (django16, django17 or django19)

    cd <repo_name>
    cp config/sample/.env config/
    mkvirtualenv <repo_name> [--python=$(which python3)]
    setvirtualenvproject
    pip install -r requirements/development.txt
    python project/manage.py syncdb
    python project/manage.py runserver

Edit `config/.env` with your setting values.

Project comes with no external DBMS configured (uses default sqlite db).

To install a database:

* add ``psycopg2`` to ``requirements/common.txt``
* uncomment ``DATABASE_URL`` line in ``config/.env`` (setting DB_NAME)
* create db
* launch migrate

.. code-block:: bash

    createdb -Upostgres DB_NAME
    python project/manage.py migrate


Other templates
---------------

- https://github.com/rdegges/django-skel
- https://github.com/jezdez/django-configurations/tree/templates/1.5.x
- https://github.com/jezdez/django-configurations/tree/templates/1.6.x
- https://github.com/twoscoops/django-twoscoops-project
- https://github.com/pydanny/cookiecutter-django

.. _cookiecutter: https://github.com/audreyr/cookiecutter


