from __future__ import absolute_import
from marketapi import settings
from app.celery import app
from pip._vendor import requests
import json
from celery import Celery
from celery.schedules import crontab
#from celery.beat import Scheduler, ScheduleEntry
import time

#@app.on_after_configure.connect
#def setup_periodic_tasks(sender, **kwargs):
#    sender.add_periodic_task(10.0, get_zebpaydata(), name='every 10s')

@app.task
def get_zebpaydata():
    url = 'https://www.zebapi.com/api/v1/market/ticker/btc/inr' 
    response = requests.get(url)
    mdata = response.json()
    return mdata
