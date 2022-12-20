FROM python:3.9-slim

WORKDIR /flask_api

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 flask_api:app