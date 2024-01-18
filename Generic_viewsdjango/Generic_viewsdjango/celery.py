from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Generic_viewsdjango.settings")

app = Celery("Generic_viewsdjango")
print(app)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.worker_prefetch_multiplier = 1 
app.conf.result_expires = 1800
app.conf.broker_connection_max_retries = 3 
app.conf.broker_connection_retry=True
app.conf.broker_connection_retry_on_startup=True
app.conf.update(worker_log_color=False, worker_log_format='[%(asctime)s: %(levelname)s/%(processName)s] %(message)s')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

CELERY_TASK_ALWAYS_EAGER = False 

