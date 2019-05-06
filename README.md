Testing Class Project!
======================

This project is a starting point to learn how to do tests in a Django project


To get it running:
-----------------

1. Create a VirtualEnv (Python 3.6+)
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
