web: newrelic-admin run-program gunicorn fullstack_challenge.wsgi --workers $WEB_CONCURRENCY --worker-class gevent
worker: python manage.py rqworker high default low
clock: python clock.py