#https://projects.raspberrypi.org/en/projects/get-started-pico-w/2

import network
import socket
from time import sleep
#from picozero import pico_temp_sensor, pico_led
import machine
import rp2
import sys

ssid = 'xxxx'
password = 'xxxx'
rp2.country('DE')


def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(f'Connected on {ip}')
    return ip

ip = connect()