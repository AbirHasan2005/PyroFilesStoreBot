FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update
RUN echo y | apt-get install locales
RUN echo y | apt install build-essential
RUN apt -qq install -y --no-install-recommends \
    curl \
    git \
    gnupg2 \
    wget

RUN set -ex; \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        busybox \
	git \
	python3 \
	python3-dev \
	python3-pip \
	python3-lxml \
	pv \
	&& apt-get autoclean \
        && apt-get autoremove \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install setuptools wheel yarl multidict
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN dpkg-reconfigure locales
COPY . /app

CMD ["python3", "bot.py"]
