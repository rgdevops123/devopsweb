# devopsweb
### Dev Ops Web

### Get the code

    $ git clone https://github.com/rgdevops123/devopsweb.git
    $ cd devopsweb


### Install Python 3.6.5

    $ sudo yum -y update
    $ sudo yum -y install yum-utils

    $ sudo yum -y groupinstall development
    $ sudo yum -y install openssl-devel postfix sqlite-devel vim wget zlib-devel
    
    $ wget https://github.com/openssl/openssl/archive/OpenSSL_1_0_2l.tar.gz
    $ tar -zxvf OpenSSL_1_0_2l.tar.gz 
    $ cd openssl-OpenSSL_1_0_2l/
    
    $ ./config shared
    $ make
    $ sudo make install
    $ export LD_LIBRARY_PATH=/usr/local/ssl/lib/
    
    $ cd ..
    $ rm OpenSSL_1_0_2l.tar.gz
    $ rm -rf openssl-OpenSSL_1_0_2l/
    
    $ wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
    $ tar xJf Python-3.6.5.tar.xz
    $ cd Python-3.6.5
    
    $ ./configure
    $ make
    $ sudo make install
    
    $ cd ..
    $ rm Python-3.6.5.tar.xz
    $ sudo rm -rf Python-3.6.5


### Install Requirements

    $ sudo /usr/local/bin/pip3 install -r requirements.txt

 
### ============================================
### Running th Application

### Create a .env.sh file for flask and gunicorn.

    $ vim .env.sh
    export DEVOPSWEB_CONFIG_MODE=Production
    export MAIL_SERVER='you.email.server'
    export MAIL_PORT=your-mail-port
    export MAIL_USE_TLS=True
    export MAIL_USERNAME='your-email@example.com'
    export MAIL_PASSWORD='your-password'
    export POSTGRES_USER=your-database-user
    export POSTGRES_PASSWORD=your-database-password
    export POSTGRES_DB=your-database-name
    export SECRET_KEY='your-secret-key'
    export SQLALCHEMY_DATABASE_URI_DEBUG='sqlite:////tmp/database.db'
    export SQLALCHEMY_TRACK_MODIFICATIONS=False


### Create a .env file for docker-compose and docker --env-file option.
    $ vim .env
    DEVOPSWEB_CONFIG_MODE=Production
    MAIL_SERVER=your-mail-server   ###Set to localhost if using local Postfix Mail Server.
    MAIL_PORT=your-mail-port
    MAIL_USE_TLS=True
    MAIL_USERNAME=your-email@example.com
    MAIL_PASSWORD=your-password
    POSTGRES_USER=your-database-user
    POSTGRES_PASSWORD=your-database-password
    POSTGRES_DB=your-database-name
    SECRET_KEY=your-secret-key
    ###Use For Development###SQLALCHEMY_DATABASE_URI=sqlite:////tmp/database.db
    SQLALCHEMY_TRACK_MODIFICATIONS=False


### Source your devopsweb profile file commands "flask" and "gunicorn".

    $ . ./.env.sh


### Set FLASK APP
    $ export FLASK_APP=devopsweb.py


### Run the Application
       Using gunicorn.
    $ /usr/bin/gunicorn --config gunicorn.py devopsweb:app &

       Using flask.
    $ flask run --host=0.0.0.0 --port=5000

       Using docker.
    $ sudo docker run --env-file .env -d --rm --name devopsweb -p 5000:5000 rgdevops123/devopsweb
        --env-file .env   ### Use .env environment file.
        -d                ### Detached mode: Run the container in the background.
        --rm              ### Automatically remove the container when it exits.
        --name devopsweb  ### Name the Docker container devopsweb.
        -p 5000:5000      ### Publish a container's port. hostPort:containerPort


### ============================================
### Database Migrations
             *** Method 1 ***
       ### Source the environment file.
    $ cd ../devopsweb
    $ export FLASK_APP=devopsweb.py
    $ vim app/models.py
       ### Update Model.
    $ flask db init
    $ flask db migrate
    $ flask db upgrade

             *** Method 2 ***
        ### Source the environment file.
    $ cd ../devopsweb
    $ export FLASK_APP=devopsweb.py
    $ vim app/models.py
       ### Update Model.
    $ python3.6 manage.py db init
    $ python3.6 manage.py db migrate
    $ python3.6 manage.py db upgrade
    
