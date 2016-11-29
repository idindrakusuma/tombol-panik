#!/usr/bin/python3

import subprocess

def send_sms(dest, message):
    subprocess.Popen(['/usr/bin/gammu', 'sendsms', 'TEXT', dest,'-text', message], shell=False, stdout=subprocess.PIPE).stdout.read()


