FROM python:3.6-slim-stretch

RUN apt-get update -y
RUN apt-get install -y --fix-missing \
    build-essential \
    python3-pip

RUN pip3 install tweepy

COPY . /root/app

CMD cd /root/app && \
    python3 main.py