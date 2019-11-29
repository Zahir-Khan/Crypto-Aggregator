import os
import django


os.environ["DJANGO_SETTINGS_MODULE"] = "marketapi.settings"

django.setup()

from app.tasks import get_zebpaydata
import app
from app import tasks
import time


if __name__ == '__main__':
    result = get_zebpaydata.delay()
    print('done')
    

