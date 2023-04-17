#Download base image ubuntu 20.04
FROM ubuntu:20.04

RUN apt-get update
RUN apt-get update -y

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y


WORKDIR /app 

RUN pip install psycopg2-binary
COPY /requirements/requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

#CMD ["python3", "__main__.py"]
ENTRYPOINT ["gunicorn", "-w", "3", "-b", ":7554", "-t", "360", "--reload", "wsgi:app"]