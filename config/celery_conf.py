from celery import Celery
from datetime import timedelta
import os


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = 'amqp://rabbitmq'
app.conf.result_backend = 'rpc://'
app.conf.result_serializer = 'json'
app.conf.task_serializer = 'pickle'
app.conf.accept_content = ['json', 'pickle']
app.conf.result_expires = timedelta(days=1)
app.conf.task_always_eager = False
app.conf.wroker_prefetch_multiplier = 1