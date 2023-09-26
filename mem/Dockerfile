FROM python:3.10.9-slim-buster

COPY . /mem_app
WORKDIR /mem_app

RUN pip install psutil flask

EXPOSE 9009

ENV THRESHOLD=19000000000
CMD ["python", "run.py"]
