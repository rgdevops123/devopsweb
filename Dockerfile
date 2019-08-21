FROM rgdevops123/rgcentos7.6

ARG APPDIR="/devopsweb/"
WORKDIR ${APPDIR}

ENV FLASK_APP devopsweb.py

RUN yum -y install firefox

COPY config.py devopsweb.py docker-run.sh gunicorn.py requirements.txt ${APPDIR}
COPY app app
COPY migrations migrations
COPY tests_pytests tests_pytests
COPY tests_selenium tests_selenium
COPY tests_unittests tests_unittests

RUN /usr/bin/pip3 install -r requirements.txt

EXPOSE 5000
EXPOSE 25

ENTRYPOINT ["/devopsweb/docker-run.sh"]
