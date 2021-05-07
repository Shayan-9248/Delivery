from celery import Celery
from datetime import timedelta
import os


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

celery_app = Celery('config')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = 'amqp://guest:guest@localhost:5672/'
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.result_serializer = 'json'
celery_app.conf.task_serializer = 'pickle'
celery_app.conf.accept_content = ['json', 'pickle']
celery_app.conf.result_expires = timedelta(days=1)
celery_app.conf.task_always_eager = False
celery_app.conf.wroker_prefetch_multiplier = 1