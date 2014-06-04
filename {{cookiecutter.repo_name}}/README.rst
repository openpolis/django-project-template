{{cookiecutter.project_name}}
=============================

{{cookiecutter.description}}

Vedi la cartella `project/` per il codice sorgente.

Vedi la cartella `docs/` per la documentazione completa del progetto.

Development
-----------

Clona questo repository, entra nella cartella creata poi esegui:

::

    $ pip install -r requirements/development.txt
    $ python project/manage.py runserver

Testing
-------

To start all Django TestCase modules:

::

    $ python project/manage.py test

To start functional test with selenium:

::

    $ python project/manage.py test tests.functional_tests

License
-------

Vedi il file LICENSE.txt
Vedi gli autori di questo progetto nel file CONTRIBUTORS.txt


-----

Generated with `cookiecutter`_ and `openpolis`_ /`django16-template`_ 0.1


.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _openpolis: https://github.com/openpolis
.. _django16-template: https://github.com/openpolis/django16-template