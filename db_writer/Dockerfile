FROM ubuntu
COPY ./writer.py /app/writer.py
RUN apt-get update
RUN apt-get install -y mysql-client python3-pip
RUN pip3 install mysql-connector-python tabulate
CMD ["/usr/bin/python3", "/app/writer.py"]
