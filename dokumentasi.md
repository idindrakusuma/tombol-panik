# Tombol Panik

## Senin, 28 November 2016
### 1. install raspbian cli only
* keyboard salah layout. terbukti dengan karakter | tergantikan dengan karakter lain di keyboard.
  Penyelesaian:
  1. `~$ sudo raspi-config`
  2. pilih `5. internationalisation...`
  3. setting locale ke `en_US.UTF-8` (sebelumnya `en_GB`)
  4. setting keyboard layout ke `Generic 105-key (Intl) PC` -> `English (US)`

### 2. aktifkan sshd
* aktifkan sshd agar dapat diremote melalui komputer lain

  `~$ sudo raspi-config` -> `Advanced Option` -> `SSH`

### 3. setting IP
* konfigurasi `/etc/wpa_supplicant/wpa_supplicant.conf` (lihat file `files/wpa_supplicant.conf`)
* konfigurasi `/etc/network/interfaces` (lihat file `files/interfaces`)
* nonaktifkan dhcpd, aktifkan standar networking Debian:
  
  `~$ sudo systemctl disable dhcpd`

  `~$ sudo systemctl enable networking`

  `~$ sudo reboot`
* IP wlan0 raspberry pi: `192.168.43.5`
* IP eth0 raspberry pi: `192.168.10.10`
* links:
  `https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md`

  `https://www.modmypi.com/blog/tutorial-how-to-give-your-raspberry-pi-a-static-ip-address`

  `http://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip`

## Selasa, 29 November 2016
### 1. switch huawei modem to 'modem' mode
* USB modem Huawei yang ada (seri tidak diketahui) tidak bisa langsung digunakan karena tidak langsung terdeteksi sebagai modem.

  konfigurasi `/etc/usb_modeswitch.conf` (lihat file `files/usb_modeswitch.conf`)

* test dengan `sudo usb_modeswitch -c /etc/usb_modeswitch.conf`
* link: `http://www.linuxslaves.com/2015/11/how-to-install-and-configure-huawei-e353-usb-modem-dongle-on-ubuntu.html`
