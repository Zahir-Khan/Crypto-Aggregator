from __future__ import absolute_import, unicode_literals
from _datetime import timedelta
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketapi.settings')

app = Celery('app',
             broker='amqp://zahir:dJango1@localhost:5672/zahir',
             backend='db+mysql://admin:HAL9000@localhost/marketdb/',)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.CELERYBEAT_SCHEDULE = {
    'add-every-20-seconds': {
        'task': 'tasks.get_zebpaydata',
        'schedule': timedelta(seconds=20),
        'args': ()
    },
}
app.conf.timezone = 'UTC'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

