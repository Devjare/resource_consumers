FROM python:3.10.9-slim-buster

LABEL author=devjare

COPY . /cpu_app
WORKDIR /cpu_app

RUN pip install -r requirements.txt

CMD ["python", "run.py"]
