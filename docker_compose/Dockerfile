FROM ubuntu:trusty

RUN apt update
RUN apt-get install -y python-pip
RUN apt-get install -y wkhtmltopdf

ADD requirements-pip .

RUN pip install -r requirements-pip

EXPOSE 5000

# Create working directory
RUN mkdir /opt/bill-shelter
WORKDIR /opt/bill-shelter
