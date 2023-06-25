import os

class Config:
    DEBUG = True
    SECRET_KEY = 'very_very_secure_and_secret'


    CELERY_BROKER_URL = os.getenv("CELERY_BROKER", 'pyamqp://guest:guest@localhost:5672//')
    CELERY_RESULT_BACKEND = os.getenv("CELERY_BACKEND", 'rpc://guest:guest@localhost:5672//')


    # if DEBUG:
    #     print ('debug is true')
    #     #### rabbit mq #### 
    #     # CELERY_BROKER_URL = 'pyamqp://guest:guest@localhost:5672//'
    #     # CELERY_RESULT_BACKEND = 'rpc://guest:guest@localhost:5672//'

    #     CELERY_BROKER_URL = os.getenv("CELERY_BROKER", 'pyamqp://guest:guest@localhost:5672//')
    #     CELERY_RESULT_BACKEND = os.getenv("CELERY_BACKEND", 'rpc://guest:guest@localhost:5672//')


    # else:
    #     print ('debug is false')
    #     ### redis #### 
    #     CELERY_BROKER_URL = 'redis://localhost:6379/0'
    #     CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


    # buy pendle and eth (growing extremely rapidly) and a very very large market potential in interest rate swaps
    # buy some frax and leave it in convex (they are only 0.2B behind uniswap and only deal with stable swaps - so they are still the king) - https://youtu.be/4A_-_gkPC14?t=189
    # if you think that curve has potential consider concex owning 50% of curve and than frax owning 7% of convex


