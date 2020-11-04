FROM ubuntu
COPY ./web.py /app/web.py
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install mysql-connector-python tabulate Flask
CMD ["/bin/python3", "/app/web.py"]