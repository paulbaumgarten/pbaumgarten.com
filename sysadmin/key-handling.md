# API key handling

## Preamble

It is generally considered bad programming practice to put security/access codes (such as passwords, API-keys) directly in your programming code. Any one who has access to your program code will be able to see these security details. The way that Python programs are run on computers means the program code is visible "enough" to any experienced programmer so you should never have these details in a Python program.

The next most obvious solution might be to put the security information in a separate file that your program loads from. The problem is this file, especially if stored in the same folder as your program code, creates other security issues. This is especially so if you start using a service like Github (hint: once you have gained enough experience as a programmer to be creating "real" projects this is something you should be looking into).

One common solution to all this, especially if you are creating a "server application", is to store your security information in the "system environment variables". That way they aren't stored in a file that is assocated with your project, and your entire code base can be safely shared with others without exposing these valuable codes.

If none of the above makes much sense to you, don't worry, it simply means this page is not for you *yet* (but it will be here waiting for you when you are).

## Setting your environment variables

### Linux

Create a file in `/etc/profile.d/PROJECTNAME.sh` for your project

```bash
#!/bin/bash
GOOGLE_API_KEY="my-google-api-key-goes-here"
FACEBOOK_API_KEY="my-facebook-api-key-goes-here"
export $GOOGLE_API_KEY
export $FACEBOOK_API_KEY
```

### Linux system service

Refer to the [systemd service instructions page](/raspberrypi/services)

### Mac OS

Edit the file  `/etc/profile`, adding the above example script for your project

### Windows

Control Panel → System and Security → System → Advanced system settings → Environment variables.

Credits: https://unix.stackexchange.com/q/26150, https://superuser.com/q/949560

### Nginx

You define the variables from within your nginx configuration.

```
 location / {
            uwsgi_param             UWSGI_SCRIPT            webapp;
            uwsgi_param             UWSGI_CHDIR             /usr/local/www/app1;
    }
```

Credit: https://stackoverflow.com/a/24349206

### Docker

You can pass environment variables to your containers with the -e flag.

An example from a startup script:

```bash
sudo docker run -d -t -i -e REDIS_NAMESPACE='staging' \ 
-e POSTGRES_ENV_POSTGRES_PASSWORD='foo' \
-e POSTGRES_ENV_POSTGRES_USER='bar' \
-e POSTGRES_ENV_DB_NAME='mysite_staging' \
-e POSTGRES_PORT_5432_TCP_ADDR='docker-db-1.hidden.us-east-1.rds.amazonaws.com' \
-e SITE_URL='staging.mysite.com' \
-p 80:80 \
--link redis:redis \  
--name container_name dockerhub_id/image_name
```

Or, if you don't want to have the value on the command-line where it will be displayed by ps, etc., -e can pull in the value from the current environment if you just give it without the = as per....

```
docker run  [...] -e PASSWORD [...]
```

If you have many environment variables and especially if they're meant to be secret, you can use an env-file:

```
$ docker run --env-file ./env.list ubuntu bash
```

The --env-file flag takes a filename as an argument and expects each line to be in the VAR=VAL format, mimicking the argument passed to --env. Comment lines need only be prefixed with #

Credit: https://stackoverflow.com/a/30494145

## Accessing your environment variables

### Python

Method 1: Will raise an exception if the key does not exist:

```python
import os
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
```

Method 2: Will return `None` if the key does not exist:

```python
import os
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
```

Method 3: Will return the provided default value if the key does not exist:

```python
import os
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', default_value)
```

Credit: https://stackoverflow.com/a/4907053

### Java

