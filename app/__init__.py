from celery import Celery
from .config import Config

def make_celery(app_name=__name__):
    # backend = "redis://localhost:6379/0"
    # broker = backend.replace("0", "1")

    broker = Config.CELERY_BROKER_URL
    backend = Config.CELERY_RESULT_BACKEND

    return Celery(app_name, backend=backend, broker=broker)

celery = make_celery()
