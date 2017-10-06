Django-project-template
=======================

A `cookiecutter`_ template for Django.

Version: 0.1

Features
--------

* Python 2.7, 3.4 or 3.5
* Django 1.11
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
    # use option --checkout for specific branch (django16, django17, django19, django110)
    # defaults to default branch (django111)

    cd <repo_name>
    cp config/sample/.env config/
    mkvirtualenv <repo_name> 
    # use option --python=$(which python3) to create a python3 virtualenv
    setvirtualenvproject
    pip install -r requirements/development.txt
    python project/manage.py migrate
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


Notes to use geodjango:

* follow instructions to install geolibraries: https://docs.djangoproject.com/en/1.11/ref/contrib/gis/install/geolibs/

Django will produce the following error when trying to execute any commands:

    django.contrib.gis.geos.error.GEOSException: Could not parse version info string "3.6.2-CAPI-1.10.2 4d2925d6"

To correct this, a single modification is needed in the django distribution:

.. code-block:: python

    def geos_version_info():
        """
        Returns a dictionary containing the various version metadata parsed from
        the GEOS version string, including the version number, whether the version
        is a release candidate (and what number release candidate), and the C API
        version.
        """
        ##
        ## this line needs to be patched
        ##
        ver = geos_version().decode().split(' ')[0]
        m = version_regex.match(ver)
        if not m:
            raise GEOSException('Could not parse version info string "%s"' % ver)
        return {key: m.group(key) for key in (
            'version', 'release_candidate', 'capi_version', 'major', 'minor', 'subminor')}


Other templates
---------------

- https://github.com/rdegges/django-skel
- https://github.com/jezdez/django-configurations/tree/templates/1.5.x
- https://github.com/jezdez/django-configurations/tree/templates/1.6.x
- https://github.com/twoscoops/django-twoscoops-project
- https://github.com/pydanny/cookiecutter-django

.. _cookiecutter: https://github.com/audreyr/cookiecutter


