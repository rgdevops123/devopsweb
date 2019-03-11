FROM centos:centos7.6.1810

ENV FLASK_APP devopsweb.py

COPY devopsweb.py gunicorn.py requirements.txt config.py .env ./
COPY app app
COPY migrations migrations

RUN yum -y update
RUN yum -y install epel-release && yum clean all

RUN yum -y groupinstall development
RUN yum -y install openssl-devel sqlite-devel vim wget zlib-devel

RUN wget --quiet https://github.com/openssl/openssl/archive/OpenSSL_1_0_2l.tar.gz > /dev/null 2>&1 && \
tar -zxvf OpenSSL_1_0_2l.tar.gz && \
cd openssl-OpenSSL_1_0_2l && \
./config shared > /dev/null 2>&1 && \
make > /dev/null 2>&1 && \
make install > /dev/null 2>&1 && \
export LD_LIBRARY_PATH=/usr/local/ssl/lib/ 

RUN wget --quiet https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz > /dev/null 2>&1 && \
tar xJf Python-3.6.5.tar.xz && \
cd Python-3.6.5 && \
./configure > /dev/null 2>&1 && \
make > /dev/null 2>&1 && \
make install > /dev/null 2>&1

RUN /usr/local/bin/pip3 install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "--config", "gunicorn.py", "devopsweb:app"]
