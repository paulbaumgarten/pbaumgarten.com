<!-- TITLE: Python Flask Nginx -->
<!-- SUBTITLE: Serving Flask applications with uWSGI and nginx -->

# Serving Flask applications with uWSGI and nginx

## Install

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y python3-pip python-dev nginx
```

## Create and start the virtual environment

```bash
sudo pip3 install virtualenv
mkdir <project>
cd <project>
virtualenv projectenv
source projectenv/bin/activate		# Start
```

## Install Python dependencies into the virtual environment

```bash
pip3 install uwsgi flask
pip3 install -r requirements.txt    # if relevant
vi wsgi.py
```

As a guide, my `requirements.txt` typically includes the following:

```text
uwsgi
Flask
flask_session
flask_socketio
flask_htmlmin
Flask-OAuthlib
pymysql
exifread
Pillow
bcrypt
```

## Check wsgi.py

In your project folder, ensure you have a `wsgi.py` file. Assuming that `app` is the core class of your project in `main.py` it will only need these 3 lines. 

Note it won't actually run the `app.run()` block as wsgi does not call itself `__main__` when it runs. It's really just the import line that is used.

```python
from main import app
if __name__ == "__main__":
   app.run()
```

## Test the website

* Start interactive mode of wsgi for testing

```bash
uwsgi --socket 0.0.0.0:8080 --protocol=http -w wsgi:app
```

* Visit the website

```
http://server-address:8080
```

* Exit interactive mode of wsgi through Ctrl-C

```bash
deactivate		# Quit the venv
```

## Configure uWSGI for nginx

* Create a `project.ini` in your project folder:

```ini
[uwsgi]
module = wsgi:app
master = true
processes = 5
socket = project.sock
chmod-socket = 666
vacuum = true
die-on-term = true
```

Note:  

* With the above, the chmod-socket sets the permissions for the project.sock file which must be accessible by the nginx user. (This cost me an hour of grief one night)
* Whatever you call the socket here (ie `project.sock`) must match what you use in the nginx conf later.

## Configure systemd

```bash
sudo vi /etc/systemd/system/<project>.service
```

The contents of your `.service` file would resemble this:

```
[Unit]
Description=My great flask project
After=network.target

[Service]
User=userid
Group=groupid
WorkingDirectory=</path/to/project>
Environment="PATH=</path/to/project>/projectenv/bin"
ExecStart=</path/to/project>/projectenv/bin/uwsgi --ini project.ini

[Install]
WantedBy=multi-user.target
```

An example one:

```
[Unit]
Description=My great flask project
After=network.target

[Service]
User=pbaumgarten
WorkingDirectory=/projects/com.greatapp/app
Environment="PATH=/projects/com.greatapp/app/bin"
ExecStart=/projects/com.greatapp/app/bin/uwsgi --ini project.ini

[Install]
WantedBy=multi-user.target
```

* Enable and start the service

```bash
sudo systemctl enable <project>
sudo systemctl start <project>
```

* It should automatically start up at system start now too! Nice :-)

## Configure nginx

The key parts for wsgi are the `include` and `uwsgi_pass` lines.

```
server { 
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name islpics.online;
    ssl_certificate /etc/letsencrypt/live/islpics.online/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/islpics.online/privkey.pem;
 
    location / { 
        include uwsgi_params;
        uwsgi_pass unix:/srv/online.islpics/app/project.sock;
        access_log on;
        error_log on;
    } 
}
```
	
* Restart nginx and you should be up and running
