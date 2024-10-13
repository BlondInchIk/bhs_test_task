FROM python:3.12.2-alpine3.19

WORKDIR /app

COPY . .

RUN pip3 install flask

RUN pip3 install mysql-connector-python

CMD ["python3", "app.py"]
