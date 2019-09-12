<!-- TITLE: Raspberry Pi: Enterprise Wifi -->
<!-- SUBTITLE: A sample configuration for connecting to an Enterprise Wifi network-->


This has been tested on Raspberry Pi 3 running Raspbian 2018-06-27.

# Sample configuration

**setup-wifi.sh**  

```bash
echo "Will setup wireless networking for ISL wireless lan"
echo "....."

# Shut down the network interfaces
echo "Disabling network interfaces..."
sudo ifdown etho0
sudo ifdown wlan0

# Copy files
echo "Copying wpa_supplicant.conf..."
sudo cp wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf
echo "Copying interfaces conf..."
sudo cp interfaces /etc/network/interfaces
echo "Copying ISL wifi security certificate..."
sudo cp isl_ch_wifi.pem /etc/ssl/certs/isl_ch_wifi.pem

# Power up the network interfaces
echo "Enabling network interfaces..."
sudo ifup wlan0

echo "Check messages above. If no issues, please reboot."
```

**wpa_supplicant.conf**  

```txt
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
	ssid="ISL"
	scan_ssid=1
	key_mgmt=WPA-EAP
	group=CCMP
	eap=PEAP
	identity="---your-username-here---"
	password="---your-password-here---"
	ca_cert="/etc/ssl/certs/isl_ch_wifi.pem"
	phase1="peapver=0"
	phase2="auth=MSCHAPV2"
}
```

**interfaces**

```txt
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

iface eth0 inet manual

allow-hotplug wlan0
iface wlan0 inet manual
    pre-up wpa_supplicant -B -Dwext -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    post-down killall -q wpa_supplicant

allow-hotplug wlan1
iface wlan1 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```



