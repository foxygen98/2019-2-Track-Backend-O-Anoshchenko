FROM python:3
RUN mkdir /ms
ADD . /ms
RUN pip3 install -r /ms/requirements.txt
WORKDIR /ms
EXPOSE 8090
CMD python3 /ms/server.py
