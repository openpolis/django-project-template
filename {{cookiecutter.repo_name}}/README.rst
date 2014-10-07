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
    $ python project/manage.py syncdb
    $ python project/manage.py runserver

Configura il file `config/.env` con i parametri necessari a far partire l'applicazione.

Testing
-------

Per avviare tutti i moduli TestCase Django:

::

    $ python project/manage.py test

Per avviare i test funzionali con selenium:

::

    $ python project/manage.py test tests.functional_tests

License
-------

Vedi il file LICENSE.txt
Vedi gli autori di questo progetto nel file CONTRIBUTORS.txt