FROM rgdevops123/rgcentos7.6

ENV FLASK_APP devopsweb.py

COPY config.py devopsweb.py gunicorn.py requirements.txt .env ./
COPY app app
COPY migrations migrations

RUN /usr/local/bin/pip3 install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "--config", "gunicorn.py", "devopsweb:app"]
