# devopsweb
### Dev Ops Web

### Get the code

    $ git clone https://github.com/rgdevops123/devopsweb.git
    $ cd devopsweb


### Install Python 3

    $ sudo yum -y update
    $ sudo yum -y install yum-utils
    $ sudo yum -y groupinstall development
    $ sudo yum -y install python3

    $ python3 -V
        Python 3.7.1


### Install requirements

    $ sudo pip3 install -r requirements.txt


####   *** Running th Application ***
    ============================================
       *** Update the .env file entries ***
    $ vim .env
    DEVOPSWEB_CONFIG_MODE=Production
    MAIL_SERVER='smtp.example.com'
    MAIL_PORT=your-mail-port
    MAIL_USE_TLS=True
    MAIL_USERNAME='your-email@example.com'
    MAIL_PASSWORD='your-password'
    POSTGRES_USER=your-database-user
    POSTGRES_PASSWORD=your-database-password
    POSTGRES_DB=your-database-name
    SECRET_KEY='your-secret-key'
    ###Use For Development###SQLALCHEMY_DATABASE_URI='sqlite:////db/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


### Create a devopsweb profile file.

    $ vim .devopsweb_profile
    export DEVOPSWEB_CONFIG_MODE=Debug
    export MAIL_SERVER='you.email.server'
    export MAIL_PORT=your-mail-port
    export MAIL_USE_TLS=True
    export MAIL_USERNAME='your-email@example.com'
    export MAIL_PASSWORD='your-password'
    export POSTGRES_USER=your-database-user
    export POSTGRES_PASSWORD=your-database-password
    export POSTGRES_DB=your-database-name
    export SECRET_KEY='your-secret-key'
    export SQLALCHEMY_DATABASE_URI_DEBUG='sqlite:////db/database.db'
    export SQLALCHEMY_TRACK_MODIFICATIONS=False


### Source your devopsweb profile file.

    $ . ./.devopsweb_profile


###   *** Set FLASK_APP ***
    $ export FLASK_APP=devopsweb.py


###   *** Run the Application ***
    $ flask run --host=0.0.0.0 --port=5000



    ============================================

###   *** Database Migrations ***
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
    
