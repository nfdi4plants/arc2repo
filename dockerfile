# syntax=docker/dockerfile:1

FROM python:3.10.2-slim-buster
WORKDIR /arc2repo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "ena-converter.py"]