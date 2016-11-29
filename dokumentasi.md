# Tombol Panik

## Tanggal tidak diketahui
### 1. Fungsikan Smartphone jadi GPS Server
...
### 2. Ambil data GPS dari Smartphone lewat skrip python
...

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

### 3. konek otomatis ke jaringan WiFi
* konfigurasi `/etc/wpa_supplicant/wpa_supplicant.conf` (lihat file `files/wpa_supplicant.conf`)

### 4. setting IP statik
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
### 1. switch modem huawei ke mode 'modem' (awalnya terdeteksi jadi USB Storage)
* USB modem Huawei yang ada (seri tidak diketahui) tidak bisa langsung digunakan karena tidak langsung terdeteksi sebagai modem.

  konfigurasi `/etc/usb_modeswitch.conf` (lihat file `files/usb_modeswitch.conf`)

* tes dengan `sudo usb_modeswitch -c /etc/usb_modeswitch.conf`

* perangkat sudah muncul di `/dev/ttyUSB0`, `/dev/ttyUSB1`, dan `/dev/ttyUSB2`.

  yang akan digunakan adalah `/dev/ttyUSB0` (coba-coba saja)

* link: `http://www.linuxslaves.com/2015/11/how-to-install-and-configure-huawei-e353-usb-modem-dongle-on-ubuntu.html`

## Rabu, 30 November 2016
### 1. Kirim SMS lewat skrip python
* Install gammu (aplikasi kirim SMS)

  `~$ sudo apt install gammu`

* buat konfigurasi gammu

  jalankan `~$ gammu-config`

  ubah isi `.gammurc` yang ada di `home` (lihat `files/.gammurc`)

* buat modul python untuk kirim sms (lihat `send_sms.py`)

  menggunakan gammu cli

* link:

  `http://stackoverflow.com/questions/89228/calling-an-external-command-in-python`

  jika menggunakan python-gammu `https://wammu.eu/python-gammu/`

### 2. Otomatisasi switch mode-nya usb_modeswitch dengan udev rules
* buat file `/etc/udev/rules.d/41-usb_modeswitch.rules`

  isi dengan: `ATTRS{idVendor}=="12d1", ATTRS{idProduct}=="1446", RUN+="/usr/sbin/usb_modeswitch -c /etc/usb_modeswitch.conf"`

  `12d1` adalah kode vendor usb, `1446` adalah kode product usb. Keduanya bisa dilihat dari `~$ lsusb`

  misalnya dari contoh keluaran berikut: `Bus 001 Device 006: ID 12d1:1446 Huawei Technologies Co., Ltd.`

* link:

  `https://www.raspberrypi.org/forums/viewtopic.php?t=32307`

  `http://askubuntu.com/questions/673618/udev-doesnt-run-bash-script-as-run-argument`
