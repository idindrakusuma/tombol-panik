# Tombol Panik

## Senin, 28 November 2016
### 1. install raspbian cli only
### 2. setting IP
* konfigurasi `/etc/wpa_supplicant/wpa_supplicant.conf` (lihat file `files/wpa_supplicant.conf`)
* konfigurasi `/etc/network/interfaces` (lihat file `files/interfaces`)
* nonaktifkan dhcpd, aktifkan standar networking Debian:
  `~$ sudo systemctl disable dhcpd`
  `~$ sudo sustemctl enable networking`
  `~$ sudo reboot`
* IP wlan0 raspberry pi: `192.168.43.5`
* links:
  `https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md`
  `https://www.modmypi.com/blog/tutorial-how-to-give-your-raspberry-pi-a-static-ip-address`
  `http://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip`
