FROM python:alpine

WORKDIR /app

COPY . /app

RUN python setup.py develop

CMD ['python',  'main.py']

EXPOSE 5002
