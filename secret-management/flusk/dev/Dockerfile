# Dockerfile
FROM python:3.9.19-slim

WORKDIR /app

COPY app.py /app

RUN pip install flask

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=127.0.0.1", "--port=5000"]