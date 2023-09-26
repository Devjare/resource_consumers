FROM python:3.10.9-slim-buster

LABEL author=devjare

COPY . /fs_app
WORKDIR /fs_app

EXPOSE 9007

RUN pip install -r requirements.txt

CMD ["python", "run.py"]
