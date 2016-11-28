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
