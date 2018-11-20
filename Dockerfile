FROM python:2.7-alpine
LABEL maintainer="lose.thoba@gmail.com" 

RUN apk update \
    && apk upgrade \
    && pip install -U pip \
    && mkdir /code

COPY requirements.txt /code

WORKDIR /code

RUN pip install -r requirements.txt

COPY . /code

EXPOSE 5000

CMD ["python", "main.py"]
