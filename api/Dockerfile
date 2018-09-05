FROM python:3.7

COPY . /api
WORKDIR /api
RUN pip install pipenv
RUN pipenv install --system

EXPOSE 5000