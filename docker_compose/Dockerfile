FROM ubuntu:trusty

RUN apt update
RUN apt-get install -y python-pip
RUN apt-get install -y wkhtmltopdf
RUN apt-get install -y xvfb
RUN printf '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf -q $*' > /usr/bin/wkhtmltopdf.sh & chmod a+x /usr/bin/wkhtmltopdf.sh &ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf

ADD requirements-pip .

RUN pip install -r requirements-pip

EXPOSE 5000

# Create working directory
RUN mkdir /opt/bill-shelter
WORKDIR /opt/bill-shelter
