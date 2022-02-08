FROM adoptopenjdk:11-jre-hotspot

RUN apt-get update -y && \
    apt-get install -y python3.8 python3-flask && \
	alias python='python3.8' 


RUN mkdir -p /opt/flask

WORKDIR /opt/flask

COPY . /opt/flask

EXPOSE 5000

ENTRYPOINT [ "python3.8" ]

CMD [ "app.py" ]