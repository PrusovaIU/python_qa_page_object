FROM python:3.9
MAINTAINER Iulia Prusova
COPY . /tests_project
WORKDIR /tests_project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["./docker_run.sh"]
