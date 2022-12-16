FROM python:3.10.9-slim-buster

COPY . /mem_app
WORKDIR /mem_app

RUN pip install psutil

CMD ["python", "mem_consumer.py"]
