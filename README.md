
# Run on local
- cd celery_docker_tofix
- python3 -m venv venv
- pip install -r requirements.txt
- python3 run.py
- Go to - http://127.0.0.1:5000
- Go to - http://127.0.0.1:5000/test/

# Run on docker-compose
- cd celery_docker_tofix
- python3 -m venv venv
- pip install -r requirements.txt
- docker-compose build
- docker-compose up
- Go to - http://127.0.0.1:5000
- Go to - http://127.0.0.1:5000/test/
