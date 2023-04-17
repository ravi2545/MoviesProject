#Download base image ubuntu 20.04
FROM ubuntu:20.04

RUN apt-get update
RUN apt-get update -y

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y


WORKDIR /app 