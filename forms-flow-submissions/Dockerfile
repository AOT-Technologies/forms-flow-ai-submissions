#Author: Kurian Benoy
FROM python:3.9-slim-buster

WORKDIR /forms-flow-submissions/app
COPY requirements.txt .
ENV PATH=/venv/bin:$PATH

RUN : \
    && python3 -m venv /venv \
    && pip install --upgrade pip \
    && pip install -r requirements.txt 

ADD . /forms-flow-submissions/app
RUN pip install -e .

EXPOSE 5000
RUN chmod u+x ./entrypoint
ENTRYPOINT ["/bin/sh", "entrypoint"]
