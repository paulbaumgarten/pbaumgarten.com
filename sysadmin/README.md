# System Adminstration notes

Various how-to guides related to administering systems for hosting projects.

## System services

* [SSH how-to](ssh-howto.md)
* [Linux terminal commands](terminal-commands.md)
* [Windows services](https://stackoverflow.com/a/46450007/10971929)

## New service setup

* [Flask server setup](https://github.com/paulbaumgarten/flask-server-setup) - This is a Python script to automate the process of:
   * Create new application folder with empty flask main.py 
   * Create venv for that application
   * Create uwsgi.py
   * Create project.ini for uwsgi
   * Install a systemd service
   * Create an nginx subdomain in sites-available
   * Setup Lets Encrypt for that subdomain

## Git related

* [Github Desktop how-to](github-desktop-how-to.pdf)
* [Github Terminal how-to](github-terminal-how-to.pdf)
* [Git other issues how-to](git-howto.md)

## File system 

* [Remove .dstore files](remove-dstore-files.sh) (bash script)
* [Remove ?icon files](remove-icon-files.sh) (bash script)
* [Disk space usage report](disk-space-usage-report.py) (Python script to find 200 largest files)
