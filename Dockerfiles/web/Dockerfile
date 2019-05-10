FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common wget
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php
RUN apt-get update

RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN apt-get update
RUN apt-get install -y apache2 curl php5.6 php5.6-dev php5.6-mysql php5.6-xml php5.6-soap php5.6-curl php5.6-gd php5.6-intl php5.6-imagick php5.6-imap php5.6-mcrypt php5.6-memcache  php5.6-pspell php5.6-recode php5.6-sqlite3 php5.6-tidy php5.6-xmlrpc php5.6-xsl php5.6-mbstring php5.6-gettext php5.6-xml php5.6-zip xvfb openjdk-9-jre-headless unzip

ADD ./apache2.conf /etc/apache2/apache2.conf
ADD ./php.ini /etc/php/5.6/apache2/php.ini

#RUN wget http://pear.php.net/go-pear.phar
RUN wget https://github.com/pear/pearweb_phars/raw/master/go-pear.phar
RUN php5.6 go-pear.phar
RUN sed -i "$ s|\-n||g" /usr/bin/pecl
RUN sed -i "s/\/usr\/bin\/php/\/usr\/bin\/php5.6/g" /usr/bin/pecl
RUN pecl -d php_suffix=5.6 install xdebug-2.5.5

# Install phpmetrics
RUN curl -L https://github.com/phpmetrics/PhpMetrics/releases/download/v2.3.2/phpmetrics.phar -o phpmetrics.phar
RUN chmod +x phpmetrics.phar && mv phpmetrics.phar /usr/local/bin/phpmetrics

ENTRYPOINT a2enmod rewrite && service apache2 restart && bash
