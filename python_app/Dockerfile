# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY python_app/requirements.txt python_app/requirements.txt
RUN pip3 install -r python_app/requirements.txt

COPY . .

ENV FLASK_APP=app.py

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
