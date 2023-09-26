FROM python:3.10.9-slim-buster

LABEL author=devjare

COPY . /net_app
WORKDIR /net_app

EXPOSE 9008

RUN pip install -r requirements.txt

CMD ["python", "run.py"]
