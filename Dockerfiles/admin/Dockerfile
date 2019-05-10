FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common wget git unzip

RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get install -y python-software-properties
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php
RUN apt-get update -y

RUN apt-get install -y apache2 curl php-pear php7.1-dev php7.1-zip php7.1-curl php7.1-gd php7.1-mysql php7.1-mcrypt php7.1-xml php7.1-mbstring libapache2-mod-php7.1

ADD ./apache2.conf /etc/apache2/apache2.conf
ADD ./php.ini /etc/php/7.1/apache2/php.ini

ENTRYPOINT a2enmod rewrite && service apache2 restart && bash
