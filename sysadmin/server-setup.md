
# Server setup procedure

## Create and connect to your server

Create a set of ssh keys (if you don't have existing ones) to use for authenticating with your server.


```bash
ssh-keygen
```

Create your server

* Create the server with a service such as Digital Ocean, Google Cloud Compute, or alternative.

* Log into your server via ssh (Mac/Linux) or Putty (Windows).

```bash
ssh root@your_server_ip
```

Create a non-root user

Give that new user sudo privleges

```bash
adduser sammy
usermod -aG sudo sammy
```

Switch your ssh key so it authenticates for this new user instead of root.

Copy your public key into your clipboard

```bash
su - sammy          # Switch to the new user
mkdir ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys     # Paste your public key
chmod 600 ~/.ssh/authorized_keys
exit                # Return to the root user
```

Disable password authentication



PermitRootLogin no

Firewall

sudo ufw app list
sudo ufw allow OpenSSH
sudo ufw enable

## Nginx and Flask


## Git sync

sudo crontab -e # To set a cron task for root

*/5 * * * * /var/www/teach.pbtools.app/update.sh

```bash
#!/bin/bash
# Run as root
cd /var/www/teach.pbtools.app/teacher-planner
su pbaumgarten -c "git fetch origin"
if ! su pbaumgarten -c "git diff --quiet origin/master"; then
	cd /var/www/teach.pbtools.app/teacher-planner
	su pbaumgarten -c "git reset --hard origin/master; git pull origin"
	echo "$(date)" >> ../update-history.txt
	/usr/sbin/service teach restart
fi
```

## Resources

Set up server, create non-root account, configure firewall

https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04

Install nginx

https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04

Secure certificates from let's encrypt

https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04

Flask and uwsgi

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04



