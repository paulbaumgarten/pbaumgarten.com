# Basic Linux and Raspberry Pi terminal commands

## Raspberry Pi specific

```bash
raspi-config					# Raspberry Pi configuration tool
raspistill -o cam.jpg			# Take a photo output to cam.jpg
raspistill -vf -hf -o cam.jpg	# Take a photo with vertical flip, horizontal flip
raspivid -t 5000 -o test.h264	# record 5 seconds of video
gpio -g mode <pin> up 			# turn on the pull up resistor for pin
gpio -g mode <pin> down 		# turn off the pull up resistor for pin
gpio -g write <pin> 0/1			# Write 0 (off) or 1 (on) to pin
gpio -g read <pin>				# Read and print the value of the pin
gpio -g readall					# Read all pins and print their numbers
```

### Examples

LED connected to pin 15 and GND. Turn on for 2 seconds

```bash
gpio -g mode 15 output
gpio -g write 15 1
sleep 2
gpio -g write 15 0
```

Detect button press on pin 14 and 3.3V

```bash
gpio -g mode 14 in
gpio -g read 14
```

* The `-g` switch uses Broadcom numbering for pins (same as all my other documentation)
* [Camera options in detail](https://www.raspberrypi.org/documentation/raspbian/applications/camera.md)
* [Understanding the pull down resistors to reduce button bounce](https://grantwinney.com/using-pullup-and-pulldown-resistors-on-the-raspberry-pi/)

For more about the gpio terminal tool, refer to [http://wiringpi.com/the-gpio-utility/](http://wiringpi.com/the-gpio-utility/)

## Files & navigating

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

## System information

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

## Compressing files

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

## Networking tools

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

## Remote connections & file transfers

```bash
# Download file
wget https://address.com/file
# SSH login to remote system
ssh <user>@<address>
# Transfer file to remote system and specified location
scp test.txt user@192.168.1.201:/home/user/     
```

## Process management

```bash
sudo service nginx restart  # restart the (for example) nginx service
sudo service nginx start    # start the (for example) nginx service
sudo service nginx stop     # stop the (for example) nginx service
ps aux   					# display currently active processes 
kill pid     				# kill process with process id (pid) 
killall proc     			# kill all processes named proc 
dmesg                       # show you every event that happened in the start sequence
```

## Permissions management

```bash
chmod 777 file 			# rwx for everyone
chmod 755 file			# rwx for owner, rx for group & world
chown userid file		# change owner of file
chown -R userid folder	# change owner of folder & it's contents
```

## Updates & upgrades

```bash
sudo apt-get update 			# Collect info on pending updates
sudo apt-get upgrade 			# Upgrade all installed packages
sudo apt-get dist-upgrade		# Upgrade the distribution if available
sudo rpi-update 				# Update the firmware (can break stuff!)
sudo apt-get install <app>      # Install the specified app
```
