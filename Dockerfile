# Get the latest OS image.
FROM rgdevops123/rgcentos7.6

# Set the Working Directory.
ARG APPDIR="/devopsweb/"
WORKDIR ${APPDIR}

# Set the FLASK_APP Environment Variable.
ENV FLASK_APP devopsweb.py

# Copy over the Application Files.
COPY config.py devopsweb.py docker-run.sh gunicorn.py requirements.txt ${APPDIR}
COPY app app
COPY migrations migrations
COPY tests_pytests tests_pytests
COPY tests_selenium tests_selenium
COPY tests_unittests tests_unittests

# Install Dependencies.
RUN pip3 install --no-cache-dir -q -r requirements.txt

# Inform Docker that the container listens on ports 25 and 5000.
EXPOSE 25
EXPOSE 5000

# Specify the command to run.
ENTRYPOINT ["/devopsweb/docker-run.sh"]
