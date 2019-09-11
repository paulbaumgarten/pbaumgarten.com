
# SSH HOW TO

## CREATE PUBLIC/PRIVATE KEYS

The public key goes to all the "hosts/servers" you want to be able to log in to. The private key stays secure with you, it IS your password.

```bash
# ssh-keygen -t rsa -b 4096 -f ~/.ssh/my-ssh-key
```

Restrict access to your my-ssh-key private key so that only you can read it and nobody can write to it. (SSH will ignore it, and you will get errors, if any other account can see the file)


```bash
# chmod 400 ~/.ssh/my-ssh-key
```

## SETUP YOUR SERVER/HOST - LINUX

2a. Copy your public key to the host - All in one line example:

```bash
# cat ~/.ssh/my-ssh-key.pub | ssh pbaumgarten@192.168.1.107 "mkdir -p ~/.ssh && cat >>  ~/.ssh/authorized_keys"
```

or manually:

* On the server, create a ~/.ssh folder
* Copy the public key to the above folder location
* Append the public key to ~/.ssh/authorised_keys in that folder

2b. Edit the following parameters in `/etc/ssh/sshd_config`

```txt
PermitRootLogin without-password
PasswordAuthentication no
Protocol 2
Port 22
```

```bash
# sudo service ssh restart
```

## SETUP YOUR CLIENT/WORKSTATION - LINUX/OSX

Check:

* Private key in your ~/.ssh folder? 
* Permissions chmod to 400? 
* Good to go!

## SETUP YOUR CLIENT/WORKSTATION - WINDOWS/PUTTY

Hostname: user@host.name.com
Connection > SSH > Auth: Private key for authentication: Browse to location of your private key.

## CONNECT - THE MANUAL METHOD - LINUX/OSX

```bash
# ssh -i ~/.ssh/my-ssh-key [USERNAME]@[IP_ADDRESS]
```

## CONNECT - THE CONFIG METHOD - LINUX/OSX

Edit your local `~/.ssh/config` file

```text
Host friendly_name_for_my_server
	IdentityFile ~/.ssh/my-ssh-key
	User pbaumgarten
	HostName your.server.com
```

Now you can use the following for an easy connection with no parameters needed!

```bash
# ssh friendly_name_for_my_server
```
