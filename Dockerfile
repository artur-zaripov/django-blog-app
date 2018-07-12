FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /djangoblogapp
WORKDIR /djangoblogapp
ADD requirements.txt /djangoblogapp/
RUN pip install -r requirements.txt
ADD . /djangoblogapp/