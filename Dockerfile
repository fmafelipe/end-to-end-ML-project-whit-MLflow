FROM python:3.11.9-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirementes.txt

CMD ["python3", "app.py"]