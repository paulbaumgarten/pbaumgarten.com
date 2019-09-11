# BASIC LINUX COMMANDS

FILES & NAVIGATING 

```bash
ls -la 					# listing of files in current folder 
cd folder 				# change directory to folder 
cd ..					# change to parent directory 
cd ~					# change to home directory 
pwd 					# print working directory 
mkdir folder			# make directory  
rm file 				# remove file/folder
rm -f file 				# force remove file/folder 
rm -r folder 			# recursively remove folder & it's contents 
cp file1 file2 			# copy filel to file2 
mv file1 file2 			# move(rename) filel to file2 
mv file1 dir/file2 		# move(rename) file1 to dir as file2 
touch file 				# create or update file 
cat file 				# output contents of file 
cat > file 				# write standard input into file 
cat >> file 			# append standard input into file 
tail -f file 			# output contents of file as it grows 
```

SYSTEM INFO 

```bash
date					# show current date/tvrne 
uptime					# show uptime 
whoami					# who you're logged in as 
w 						# display who is online 
cat /proc/cpujnfo 		# display cpu info 
cat /proc/meminfo 		# memory info 
cat /proc/partitions	# info size and number of partitions
cat /proc/version		# What version of Pi
free 					# show memory and swap usage 
du 						# show directory spaco usage 
du -sh 					# displays readable sizes in GB 
df -h					# show disk usage 
uname-a 				# show kernel config 
vcgencmd measure_temp	# show CPU temperature
free -o -h 				# show available system memory
lsusb 					# show attached USB devices
```

COMPRESSING 

```bash
tar cf file.tar files 	# tar files into filetar 
tar xf file.tar 		# untar into current directory 
tar tf file.tar 		# show contents of archive 
```

options: 

* c - create archive 
* t - table of contents 
* x - extract 
* z - use zip/gzip 
* f - specify filename 
* j - bzip2 compressed
* w - ask for comfirmation
* k - do not overwrite
* T - files from file
* v - verbose

NETWORKING 

```bash
ping www.host.com 		# ping host
whois domain 			# get whois for domain 
dig domain 				# get DNS for domain 
dig -x host 			# reserve lookup host 
wget file 				# download file 
wget -c file 			# continue stopped download 
wget -r url 			# recurively download files from url 
curl url 				# outputs tho webpage from url 
curl -o meh.html url	# writes the page to meh.html 
ssh user@host 			# connect to host as user 
ssh-p port user@host 	# connect using port 
ssh-D user@host 		# connect & use bind port 
netcat					# Network scanning 
top						# Top processes using CPU, RAM etc
iwconfig				# Show wifi network connected to
ifconfig				# Show network connection info
iwlist wlan0 scan		# Show currently available networks
nmap					# Show connected devices on your network
hostname -I 			# Show IP address of your device
netstat -l              # display all listening connections
netstat -lpc            # display all listening connections, update continuously
```

* [netcat how-to](https://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf)

REMOTE CONNECTIONS & TRANSFERS

```bash
wget https://address.com/file       # Download file
ssh <user>@<address>                # SSH login to remote system
                                    # Transfer file to remote system and specified location
scp test.txt user@192.168.1.201:/home/user/     
```

PROCESSES 

```bash
sudo service nginx restart  # restart the (for example) nginx service
sudo service nginx start    # start the (for example) nginx service
sudo service nginx stop     # stop the (for example) nginx service
ps aux   					# display currently active processes 
kill pid     				# kill process with process id (pid) 
killall proc     			# kill all processes named proc 
dmesg                       # show you every event that happened in the start sequence
```

PERMISSIONS 

```bash
chmod 777 file 			# rwx for everyone
chmod 755 file			# rwx for owner, rx for group & world
chown userid file		# change owner of file
chown -R userid folder	# change owner of folder & it's contents
```

RASPBERRY PI SPECIFIC

```bash
raspi-config					# Raspberry Pi configuration tool
raspistill -o cam.jpg			# Take a photo output to cam.jpg
raspistill -vf -hf -o cam.jpg	# Take a photo with vertical flip, horizontal flip
raspivid -t 5000 -o test.h264	# record 5 seconds of video
gpio -g mode <pin> up 			# turn on the pull up resistor for pin
gpio -g mode <pin> down 		# turn off the pull up resistor for pin
gpio -g write <pin> 0/1			# Write 0 or 1 to pin
gpio -g read <pin>				# Read and print the value of the pin
gpio -g readall					# Read all pins and print their numbers
```

* The `-g` switch uses Broadcom numbering for pins (same as all my other documentation)
* [Camera options in detail](https://www.raspberrypi.org/documentation/raspbian/applications/camera.md)
* [Understanding the pull down resistors to reduce button bounce](https://grantwinney.com/using-pullup-and-pulldown-resistors-on-the-raspberry-pi/)

UPDATES AND UPGRADES

```bash
sudo apt-get update 			# Collect info on pending updates
sudo apt-get upgrade 			# Upgrade all installed packages
sudo apt-get dist-upgrade		# Upgrade the distribution if available
sudo rpi-update 				# Update the firmware (can break stuff!)
sudo apt-get install <app>      # Install the specified app
```
