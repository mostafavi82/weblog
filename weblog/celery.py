from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weblog.settings')

app = Celery('weblog')


app.config_from_object('django.conf:settings', namespace='CELERY' )

app.autodiscover_tasks()


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'posts.views.test2',
        'schedule': 2
    },
}