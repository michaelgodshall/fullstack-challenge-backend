====================
fullstack_challenge README
====================

If this is your first project using python or virtualenv, follow the instructions in docs/setup.rst before continuing.

Install Project Dependencies
============================

NOTE: This project uses Python 3 instead of Python 2.7, which may need to be installed before you can continue.
Please follow the instructions in docs/setup.rst to install Python 3.

Create a virtualenv for the project::

    $ mkvirtualenv -p $(which python3) fullstack_challenge

You should see '(fullstack_challenge)' added to the beginning of your Terminal input line,
which indicates the 'fullstack_challenge' virtualenv is activated.

If not, activate the virtualenv.  This virtualenv must be activated whenever you work on the project::

    $ workon fullstack_challenge

Clone the project via git

Change to the root directory::

    $ cd fullstack_challenge

Install dependencies::

    $ pip install -r requirements/local.txt

Install bower dependencies (node and bower must be installed first)::

    $ bower install

Install npm dependencies (node and npm must be installed first)::

    $ npm install

Setup the database
============================
Defaults to sqllite::

    $ ./manage.py migrate

Create a superuser (optional)
============================
You will use the username and password you create in this step to login to the admin at `localhost:3000/admin/`::

    $ ./manage.py createsuperuser

Run The Server
============================
From fullstack_challenge::

    $ ./manage.py server

Your browser should open automatically to `localhost:3000`

Run these commands whenever you pull changes::

    $ pip install -r requirements/local.txt
    $ ./manage.py migrate
    $ ./manage.py server

If you prefer to run the gulp server separate from the Django backend server, open 2 Terminal windows at the root of the
project.  Run Django server in the first window::

    $ ./manage.py runserver

Then run the gulp server in the second window::

    $ gulp
