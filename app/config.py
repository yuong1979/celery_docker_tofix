import os


class Config:
    DEBUG = True
    SECRET_KEY = 'very_very_secure_and_secret'

    #### rabbit mq #### 
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER", 'pyamqp://guest:guest@localhost:5672//')
    CELERY_RESULT_BACKEND = os.getenv("CELERY_BACKEND", 'rpc://guest:guest@localhost:5672//')



    #### redis #### 
    # CELERY_BROKER_URL = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'



