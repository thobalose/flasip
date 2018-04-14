FROM python:2.7
LABEL maintainer="lose.thoba@gmail.com"

RUN apt-get update -y --fix-missing && \
    apt-get ugrade -y && \
    apt-get install git -y && \
    pip install -U pip

RUN git clone -b appegine https://github.com/thobalose/flasip.git && \
    cd flasip && \
    pip install -r requirements.txt

CMD ["python", "main.py"]
