FROM ubuntu:18.04
RUN  apt-get -y update && apt-get -y install nginx
COPY files/default /etc/nginx/sites-available/default
COPY files/index.html /usr/share/nginx/html/index.html
COPY files/style.css /usr/share/nginx/html/style.css
EXPOSE 80
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]