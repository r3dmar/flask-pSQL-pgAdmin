FROM python:3.7-alpine@sha256:e6da3ee9bb64dd12b98fa609487f112fe1e365522e6e8345309db15c22a80a51

RUN pip install flask flask-sqlalchemy psycopg2-binary

COPY . /app
WORKDIR /app

ENV FLASK_APP=flask-app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]