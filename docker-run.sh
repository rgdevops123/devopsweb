#!/bin/bash 

/usr/sbin/postfix start

#
# If using HTTPS, uncomment the below line and update with your .pem files.
# 
# gunicorn --certfile cert.pem --keyfile key.pem --config gunicorn.py devopsweb:app

#
# If using HTTP, uncomment the below line 
#
gunicorn --config gunicorn.py devopsweb:app
