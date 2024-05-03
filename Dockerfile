FROM ubuntu/mysql

COPY . /home/oasd_blog
RUN apt update
RUN apt-get -y upgrade

# INSTALL AND SETUP PYTHON
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-venv
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y pkg-config
RUN pip install mysqlclient
WORKDIR /home/oasd_blog

RUN pip install flask
RUN pip install sqlalchemy

