<!-- TITLE: Docker -->
<!-- SUBTITLE: A quick summary of Docker -->


# Docker how-to

A virtualisation tool at the per-app level. Encapsulate all your necessary libraries, dependencies etc, expose a port and run!

Jargon: A container is an instance of an image. You can run many containers of the same image (such as to load balance)

# Running images

## Create a new container/instance

Will create a new instance based on the image. If you have already created an instance before (and you aren't intentionally trying to run multiple ie: to load balance), use `docker start`

`docker run -d --name <name_of_instance> -p <external_port>:<internal_port> <author/image>`
* -d = run as a daemon (ie: in the background)
* [name_of_instance] = the name you wish to assign to the image
* external_port = what port your host machine will use to access the application
* internal_port = what port your application has been written to accept requests on
* author - the dockerhub account you are getting a project image from
* image - the dockerhub image to fetch

eg:

* `docker run -d --name helloworld -p 8080:80 tutum/hello-world`  
* `docker run python:3.6`  

## Starting an existing container/instance

`docker start <name_of_instance>`

## Stopping an container/instance

`docker stop <name_of_instance>`

## View running container/instance

`docker ps`

## View all containers/instances (including stopped instances)

`docker ps -a`

<div class="page"/>

## View all images

`docker images`

## Delete a container/instance

`docker rm <name>`

## Delete an image

`docker rmi <image>`

## Login to DockerHub (or other repo)

`docker login`

# Creating an image

Install Docker on your development machine.
https://docs.docker.com/machine/

Steps:

## Step 1. Create your project (duh...)

## Step 2. Find a suitable docker baseline image

Docker images are generally built on top of a trustworthy pre-existing image. You will reference this with the `FROM` command in your Dockerfile. Some of the more common/popular ones are:

* python
* ubuntu
* mysql
* postgres
* nginx
* torrent
* wordpress
* nextcloud

Check out `https://hub.docker.com/explore/` for more.

<div class="page"/>

## Step 3. Put a `Dockerfile` (text file) into the project root folder

**Example Dockerfile for nginx**  

```text
FROM    nginx
RUN     mkdir /etc/nginx/logs && \
        touch /etc/nginx/logs/staticlog
COPY    ./nginx.conf /etc/nginx/conf.d/defaults.conf
COPY    /src /www
EXPOSE  80
```

* `ADD` and `COPY` are more-or-less the same ting and will copy from your local project folder (where you are creating the Dockerfile), into the docker image location

**Example Dockerfile for python/flask**  

```python
# Use an official Python runtime as a parent image
FROM    python:3.6
# Add any useful labels
LABEL   maintainer="Paul Baumgarten pbaumgarten.com"
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY    . /app
# Install any needed packages specified in requirements.txt
RUN     pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE  80
# Define environment variable
ENV NAME "My amazing app"
# Run app.py when the container launches
CMD     ["python", "app.py"]
```

In this example, also create `requirements.txt` ... with a list of the packages to install with pip, eg:

```text
Flask
pymysql
flask_session
exifread
flask_socketio
flask_htmlmin
bcrypt
Pillow
```

* Note: with the setting of the environment variable above, you'd be able to easily access that in Python by importing `import os` and using `print(os.environ['NAME'])`

<div class="page"/>

**Example Dockerfile for ubuntu**  

```text
FROM    ubuntu:latest
RUN     apt-get update && apt-get install -y \
        python-pip \
        python-dev \
        build-essential \
COPY    . /app
WORKDIR /app
RUN     pip install -r requirements.txt
CMD     ["python", "app.py"]
```

* Note: Avoid RUN `apt-get upgrade` and `dist-upgrade`, as many of the “essential” packages from the parent images cannot upgrade inside an unprivileged container.

**Volumes**  

The VOLUME instruction creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers. Use this for data storage locations that you don't want to lose if you wipe/rebuild/update the image. Eg: configuraiton files, database files, client data, log files.

The host directory is declared at container run-time: The host directory (the mountpoint) is, by its nature, host-dependent. This is to preserve image portability, since a given host directory can’t be guaranteed to be available on all hosts. For this reason, you can’t mount a host directory from within the Dockerfile.

If you start a container with a volume that does not yet exist, Docker creates the volume for you.

The following simple example will create a volume `/myvol`.

```text
FROM    ubuntu
RUN     mkdir /myvol
RUN     echo "hello world" > /myvol/greeting
VOLUME  /myvol
```

When you run the image, you would specify the relevant host location using either `--mount` or `-v` as follows:

```bash
docker run -d --name devtest --mount source=myvol,target=/app nginx:latest  
## or
docker run -d --name devtest -v myvol:/app nginx:latest
```

Use `docker inspect devtest` to verify that the volume was created and mounted correctly. Look for the `Mounts` section.

<div class="page"/>

## Step 4. Build the image file

`docker build -t <project> .`
`docker build -t <project>:<tag> .`

The dot is the path to my Dockerfile

The tag is optional, think of it as the version number of your project.

## Step 5. Verify

Verify it has been built with:
`docker image ls`

## Step 6. Run it

`docker run -d --name <project_instance> -p 8080:80 <project>`

Stop it

`docker stop <project_instance>`

## Step 6. Share

Login to cloud.docker.com

`docker login`

Associate the local image with a repository on a registry

`docker tag <image> <username>/<repository>:<tag>`

Deploy to the cloud

`docker push <author>/<project>:<tag>`
`docker push <author>/<project>:<tag>`

## Tips and troubleshooting

### Logs

To check logs for a container, `docker logs container-name`

### DNS settings

Proxy servers can block connections to your web app once it’s up and running. If you are behind a proxy server, add the following lines to your Dockerfile, using the ENV command to specify the host and port for your proxy servers:
```
# Set proxy server, replace host:port with values for your servers
ENV http_proxy host:port
ENV https_proxy host:port
```

<div class="page"/>

### Proxy server settings

DNS misconfigurations can generate problems with pip. You need to set your own DNS server address to make pip work properly. You might want to change the DNS settings of the Docker daemon. You can edit (or create) the configurarion file at /etc/docker/daemon.json with the dns key, as following:
```
{
  "dns": ["your_dns_address", "8.8.8.8"]
}
```
In the example above, the first element of the list is the address of your DNS server. The second item is the Google’s DNS which can be used when the first one is not available.

Before proceeding, save daemon.json and restart the docker service.

`sudo service docker restart`

Once fixed, retry to run the build command.

### Communicating with host services

* A VLAN "bridge" is established between the host and docker containers, with their own subnet.
* On the host, `sudo ip addr show docker0` to get the the host IP address.
* Or, on the container, `ip addr show eth0` or `route` to find the host as the default gateway.
* Note: MySQL binds itself to 127.0.0.1 not 0.0.0.0. This will need to change else the container won't be able to see it. Edit `my.cnf`. Warning: Ensure firewall is blocking external access to 3306, else MySQL will be externally accessible.
* Run the following on the container to set the host IP as an environment variable, `export DOCKER_HOST_IP=$(route -n | awk '/UG[ \t]/{print $2}')`.

### Passing an environment variable to the container

To embed within the command line:  

* `sudo docker run -d -t -e MYSQL_PASSWORD='secret' -e MYSQL_HOST='192.168.1.1'`

To send the content of a matching environment variable from the host:

* `sudo docker run -d -t -e MYSQL_PASSWORD -e MYSQL_HOST`

To pass a file containing key-value pairs to set in the environment:

* `docker run --env-file ./env.list ubuntu`

<div class="page"/>

### To run an interactive docker (eg: bash)

* `docker run -t -i ubuntu`
* `-d` = Detached / daemon (re-attach with `docker attach`)
* `-t` = Allocate a TTY
* `-i` = Interactive

### MySQL

Start a mysql server instance

```bash
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```

Connect to MySQL from an application in another Docker container

* This image exposes the standard MySQL port (3306), so container linking makes the MySQL instance available to other application containers. Start your application container like this in order to link it to the MySQL container:

```bash
docker run --name some-app --link some-mysql:mysql -d application-that-uses-mysql
```

Specify a host volume location for the data files

1. Create a data directory on a suitable volume on your host system, e.g. `/my/own/datadir`.
2. Run docker by mapping that folder to `/var/lib/mysql` as follows:

```bash
docker run --name some-mysql -v /my/own/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```

Creating database dumps

```bash
docker exec some-mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /some/path/on/your/host/all-databases.sql
```

### Using bash to make changes to an image

You can run either create a Dockefile and run from the same directory where your Dockerfile is located.

* `docker build .`

or you can run:

* `docker run -i -t <docker-image> bash`

or (if your container is already running)

* `docker exec -i -t <container-id> bash`

once you are in the shell make all the changes you please. Then run:

* `docker commit <container-id> myimage:0.1`

You will have a new docker image locally myimage:0.1. If you want to push to a docker repository (dockerhub or your private docker repo) you can run:

* `docker push myimage:0.1`

## Examples

### Wordpress blog

Using the official images of mysql and wordpress to create a blog:

```bash
# Create the database storage location on the host
sudo mkdir /var/docker
sudo mkdir /var/docker/volumes
sudo mkdir /var/docker/volumes/girlscoding-mysql
# Create the mysql database container
docker run -d --name girlscoding-mysql -p 10001:3306 -v /var/docker/volumes/girlscoding-mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD="secret" mysql:5.7
# Create the wordpress container
docker run -d --name girlscoding-wordpress -p 10002:80 --link girlscoding-mysql:mysql wordpress
```

Edit nginx.conf on the host to run on a /folder entrypoint: 

```text
                location /girlscoding/ {
                        proxy_pass http://localhost:10002/;
                }
```

Edit nginx.conf on the host to run on a subdomain entrypoint: 

```text
        server {
                listen 80;
                listen [::]:80;
                listen 443 ssl;
                listen [::]:443 ssl;
                server_name girlscoding.cs.isl.ch;
                location / {
                        proxy_pass http://localhost:10002;
                        proxy_http_version 1.1;
                        proxy_set_header Upgrade $http_upgrade;
                        proxy_set_header Connection 'upgrade';
                        proxy_set_header Host $host;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_cache_bypass $http_upgrade;
                }
        }
```
