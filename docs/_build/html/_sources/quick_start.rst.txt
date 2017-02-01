Quick Start Guide
=================

Download dba16web project
-------------------------

First, you need to download the dba16web from GitHub

https://github.com/Datenbanken16/dba16-web"

Install all Components
----------------------
For this you have to install Django on your enviroment.

First install a Postgresql-Database on your own Computer.

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

Switch to the User who was created by the commands before (postgres):

.. code-block:: bash

    $ sudo su - postgres

Log into Postgres :

.. code-block:: bash

    $ psql

Now you can create your Database (!dont forget the semikolon after each operation!):

.. code-block:: bash

    $ CREATE DATABASE project;

Create a User:

.. code-block:: bash

    $ CREATE USER myUser WITH PASSWORD 'MyPassword';

Make some Setups for speeding up operations:

.. code-block:: bash

    $ ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    $ ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    $ ALTER ROLE myprojectuser SET timezone TO 'UTC';

Now the User needs access to your database:

.. code-block:: bash

    $ GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

Back to the user's shell:

.. code-block:: bash

    $ \q
    $ exit

For the REST SERVICE DJANGO-RESTFRAMEWORK you need to install:

.. code-block:: bash

    $ sudo pip install djangorestframework markdown django-filter

The django REST framework, markdown support for browsable API and filtering support

Add 'rest_framework' to your INSTALLED_APPS setting in settings.py.

.. code-block:: bash

     INSTALLED_APPS = (
         ...
         'rest_framework',
     )

If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.

.. code-block:: bash

    urlpatterns = [
        ...
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]

More Information on Django REST Framework: http://www.django-rest-framework.org/

To avoid crossite-skripting Conflicts install Django CORS Headers

.. code-block:: bash

    $ pip install django-cors-headers

make some changes in settings.py:

add to installed apps

.. code-block:: bash

    INSTALLED_APPS = (
        ...
        'corsheaders',
        ...
    )

add to middleware

.. code-block:: bash

    MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]

for now we allow all crossitescriptings

.. code-block:: bash

    CORS_ORIGIN_ALLOW_ALL = True

To use Bootstrap install the following

.. code-block:: bash

    pip install django-bootstrap3

make some changes in settings.py:

add to installed apps

.. code-block:: bash

    INSTALLED_APPS = (
        ...
        'bootstrap3',
        ...
    )

More Information on Django bootstrap3: <a href="https://django-bootstrap3.readthedocs.io">Here!</a>

After that, you can start coding with Django.

The Setup for the server you can see in YourProject/YourProject/settings.py. In our case: dba16-web/wohlfuehlprojekt/settings.py.

.. code-block:: bash

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'testdb',
            'USER': 'testadmin',
            'PASSWORD': 'qwertz',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

To start your server. Open another terminal and navigate to /etc/init.d/ and start your database with "./postgresql start". With the command "psql -l" you can see your running databases.

Apply the migrations to your database. Go into your Project (the "dba16-web" folder). And set up the initial databse structure:

.. code-block:: bash

    $ python manage.py makemigrations
    $ python manage.py migrate

Create an administrative account:

.. code-block:: bash

    $ python manage.py createsuperuser

Select a username,emailadress and password. Test youre Server:

.. code-block:: bash

    $ python manage.py runserver 127.0.0.1:8000

Visit your server in your web browser:

http://localhost:8000

How to fix the "bad magic number" error

Run from the highest directory of your project:

.. code-block:: bash

    find . -name '*.pyc' -delete
