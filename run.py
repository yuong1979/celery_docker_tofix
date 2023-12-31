#########################################################################################
##### backup of multiple file flask celery app that runs fine #############################
#########################################################################################

from app import factory
from app.config import Config
import app

app = factory.create_app(celery=app.celery)

if __name__ == "__main__":
    # app = factory.create_app(celery=app.celery)

    app.debug = Config.DEBUG

    app.run(host="0.0.0.0", port=5000)


# commands to run 
# python3 run.py
# celery -A celery_worker.celery worker --loglevel=info --pool=solo
# celery -A celery_worker.celery worker --loglevel=info --concurrency=2

# http://localhost:5000/flask_celery_howto.txt/it-works!
# http://localhost:5000/test/








# ##########################################
# ##### Running single Dockerfile (Flask) ##
# ##########################################
# 1. `cd docker_template/flask`
# 2. `docker build --tag celery-flask1 .`
# 3. `docker run --publish 5000:5000 celery-flask1`
# 4. `docker exec -it 9cb1a375b364b2999ad90e5454664153b8bf1686c01dedc415526d86d411549f /bin/bash`

# ##########################################
# ##### Running entire Docker Compose ######
# ##########################################
# 1. `cd docker_template`
# 2. `docker-compose build`
# 3. `docker-compose up`
# 4. `docker exec -it name_of_container sh`










#########################################################################################
##### backup of single file flask celery app that runs fine #############################
#########################################################################################

# from flask import Flask, flash, render_template, request, redirect, url_for
# # from flask_mail import Mail, Message
# from celery import Celery
# from app.config import Config
# from time import sleep

# app = Flask(__name__)
# app.config.from_object(Config)
# app.secret_key = app.config['SECRET_KEY']
# client = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
# client.conf.update(app.config)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         hello = complex_task.delay('task_completed')
#         print (hello)
#         return render_template('index.html')
    
# @client.task
# def complex_task(text):
#     sleep(5)
#     return text

# if __name__ == '__main__':
#     app.run(debug=True)

# commands to run 
# on terminal 1 - flask run
# on terminal 2 - celery -A app.client worker --concurrency=4 --loglevel=info
# on url - http://127.0.0.1:5000/
