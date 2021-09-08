FROM python:3.9

RUN pip install Flask Flask-Cors gunicorn

COPY src/ app/
WORKDIR /app

ENV Port 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app