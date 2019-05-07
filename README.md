Testing Class Project!
======================

This project is a starting point to learn how to do tests in a Django project

Pre-requisites:
---------------
* Mac OS (if you want to run the functional tests, which use an OS-dependent Chrome Driver)
* Python 3.6 or greater
* Chrome version 44.x (for functional tests - you can download a different version of chromedriver and install in the `bin` dir if you are on a different version)


To get it running:
-----------------

1. Create a VirtualEnv (Python 3.6+) and activate it
1. `pip install -r requirements.txt` to install Django
1. `python manage.py migrate` to init your SQLlite DB
1. `python manage.py createsuperuser`  (*username*: admin, *password*: admin (just accept the 'this is a common password' warning), *email*: admin@admin.com )
1. `python manage.py loaddata todo` to load some sample data
1. `python manage.py runserver` to start up Django (or use the `Django Server' config in PyCharm's Run Menu)
1. Browse to `http://localhost:8000` to see the app


To run tests:
-------------
1. `python manage.py test` (or use the `All Tests` config in PyCharm's Run Menu)
1. `python manage.py test project` to only run the tests in the `project` module
1. `python manage.py test todo.tests.model_tests.TestListModel.test_list_data` to run only a single specific test
1. `python ./functional_tests.py` to run the functional tests
    1. If you get an error like `requests.exceptions.InvalidSchema: No connection adapters were found for 'data:image/svg+xml` if means your Django Server is not running
1. `coverage run manage.py test; coverage report -m --omit ".venv*,*tests*,manage.py,*migrations*,*wsgi.py"` to run tests with coverage and view report
