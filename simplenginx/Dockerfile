FROM adoptopenjdk:11-jre-hotspot

RUN apt-get update -y && \
	apt-get install -y nginx

RUN mkdir -p /opt/html

ADD nginx.conf /etc/nginx/nginx.conf
ADD index.html /opt/html/index.html

EXPOSE 80
CMD ["nginx"]