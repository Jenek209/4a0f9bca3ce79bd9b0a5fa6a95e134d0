FROM python:3.6
RUN mkdir /data
WORKDIR /data
ADD requirements.txt /data
RUN pip install -r requirements.txt
ADD . /data

