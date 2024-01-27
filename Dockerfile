FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt upgrade -y && apt install vim -y && apt install python3-pip -y && apt install git -y
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "/bin/sh", "/app/start_app.sh"]