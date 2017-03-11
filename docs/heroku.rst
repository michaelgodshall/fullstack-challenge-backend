============================
Heroku Setup
============================

    $ heroku create fullstack_challenge

Heroku Environment Variables
============================

Add the following environment variables to the heroku app::

    $ heroku config:set BUILDPACK_URL=https://github.com/heroku/heroku-buildpack-multi.git
    $ heroku config:set DJANGO_DEBUG=False
    $ heroku config:set DJANGO_SETTINGS_MODULE=fullstack_challenge.settings.heroku
    $ heroku config:set WEB_CONCURRENCY=3  #  https://devcenter.heroku.com/articles/optimizing-dyno-usage#python
    $ heroku config:set NEW_RELIC_APP_NAME='fullstack_challenge'
    $ heroku config:set DJANGO_SECRET_KEY=SECRET_KEY_GOES_HERE
    $ heroku config:set DJANGO_STATIC_HOST=CLOUDFRONT_URL_GOES_HERE

Heroku Apps
============================

Add the following apps::

    $ heroku addons:create heroku-postgresql:hobby-dev
    $ heroku pg:backups schedule --at '02:00 America/Los_Angeles' DATABASE_URL
    $ heroku addons:create papertrail:choklad
    $ heroku addons:create newrelic:wayne
    $ heroku addons:create loaderio:basic
    $ heroku addons:create sendgrid:starter
    $ heroku addons:create rediscloud:30

Heroku Production Check
============================

https://devcenter.heroku.com/articles/production-check

Dyno Redundancy (https://devcenter.heroku.com/articles/production-check#dyno-redundancy)::

    Running at least 2 web dynos for any mission-critical app increases the probability that the app will remain
    available during a catastrophic event. Multiple dynos are also more likely to run on different physical
    infrastructure (for example, separate AWS Availability Zones), further increasing redundancy.

Postgres High-Availability (https://devcenter.heroku.com/articles/heroku-postgres-ha)::

    The Premium and Enterprise tiers of Heroku Postgres databases have additional benefits for application uptime,
    including High Availability with automatic failover.  Unfortunately, it's 3x the price of their standard plan ($200 vs $50).


Deploy to Production Server
============================

Deploy your local "master" branch to the "master" branch of the production server::

    $ git push heroku master

Setup Staging Server
============================

https://devcenter.heroku.com/articles/multiple-environments#starting-from-an-existing-app

Fork the production app to copy over config vars, re-provision all add-ons, and copy all Heroku Postgres data::

    $ heroku fork --from fullstack_challenge --to fullstack_challenge-staging

Add a git remote for the forked staging app::

    $ git remote add staging git@heroku.com:fullstack_challenge.git

Set the staging server as the default for heroku commands::

    $ git config heroku.remote staging

Deploy to Staging Server
============================

Deploy your local "develop" branch to the "master" branch of the staging server::

    $ git push staging develop:master

Deployment Best Practices
============================

https://docs.google.com/document/d/1RAvK_16ZHimKbN4pk7wZQzgkR8ThrSt5nB_c0A_ssBY/edit
