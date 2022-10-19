FROM python:3.9-alpine
MAINTAINER Luis Melendez

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "./django_tech_test/manage.py", "runserver", "0.0.0.0:8000"]