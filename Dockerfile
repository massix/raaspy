FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app

ADD Application.py /app/Application.py
ADD requirements.txt /app/requirements.txt
ADD model /app/model
ADD api_number /app/api_number
ADD api_string /app/api_string
ADD swagger /app/swagger

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python3 -u Application.py
