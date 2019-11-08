FROM python:3-slim

RUN apt-get update \
    && pip install -U pip \
    && mkdir /code

COPY requirements.txt /code

WORKDIR /code

RUN pip install -r requirements.txt

COPY . /code

EXPOSE 5000

CMD ["python", "run.py"]
