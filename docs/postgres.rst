=============================================
Setting up PostgreSQL for local development
=============================================

Install PostgreSQL if not installed already::

    $ brew install postgres

Run PostgreSQL as a background service::

    $ brew tap homebrew/services
    $ brew services start postgresql

Create a database::

    $ psql
    # CREATE DATABASE fullstack_challenge;
    # GRANT ALL PRIVILEGES ON DATABASE fullstack_challenge TO username;

Install Python dependencies::

    $ pip install psycopg2
