# Deploying a Flask App

Note: This guuide is probably bad and it's better to just follow this guide outright: https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

## Setting Up for mod_wsgi
First install: ```sudo apt-get install libapache2-mod-wsgi python-dev```. It may be useful to specify python version.
```sudo a2enmod wsgi``` 

## Create Flask App:
cd into desired directory with ```cd /var/www``` and make a directory with ```sudo mkdir {directory}```. 
Then go inside that folder with ```cd``` and make another directory with name {directory}. 
Then, create two more directories for you flask app with ```sudo mkdir static templates```. 
Now, create your init file with: ```sudo nano __init__.py ```. 
Note: You probably will not be able to edit the file without sudo. Fill up the flask up with legal python3 and Flask code.

Now, you will need to install flask. Create a virtual environment within the current directory, and install flask on it.

## Enable Virtual Host:
Do ```sudo nano /etc/apache2/sites-available/{appname}``` or ```sudo nano /etc/apache2/sites-available/{appname}.conf``` based on Ubuntu version (without conf worked for me)

Paste in the following:
```<VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
After saving and closing, do:
```
sudo a2ensite {appname}
cd /var/www/{appname}
sudo nano {appname}.wsgi ```

After getting into nano, paste in the following: 
```#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/{appname}/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key'
```


