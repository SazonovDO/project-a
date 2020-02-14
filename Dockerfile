FROM ubuntu:18.04

ENTRYPOINT ["python3", "/opt/main.py", "--prod"]

RUN apt update && apt -y install python3 python3-pip

COPY . /opt

RUN cd /opt/ && \
    pip3 install -r ./requirements.txt
