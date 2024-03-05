FROM python:3.6.2-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /var/log/bitcalc
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app
