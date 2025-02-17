from picodfplayer import DFPlayer
from time import sleep, ticks_ms
from machine import Pin, ADC, Timer
from sys import exit
from random import randint

#
#C:\...\DATA                     SD Card
#├───dice                        ├───02
#│       dice_1_de.mp3           │     001.mp3 
#│       dice_2_de.mp3           │     002.mp3 
#│       dice_3_de.mp3           │     003.mp3 
#│       dice_4_de.mp3           │     004.mp3 
#│       dice_5_de.mp3           │     005.mp3 
#│       dice_6_de.mp3           │     006.mp3 
#│                               │
#└───motivation                  └───01
#        motivation_1_de.mp3           001.mp3 
#        motivation_2_de.mp3           002.mp3 
#        motivation_3_de.mp3           003.mp3 
#        motivation_4_de.mp3           004.mp3 
#        motivation_5_de.mp3           005.mp3 
#        motivation_6_de.mp3           006.mp3 
#        motivation_7_de.mp3           007.mp3 

# try picozero
#https://pypi.org/project/picozero/
#from picozero import Button

#https://forums.raspberrypi.com/viewtopic.php?t=373972
ldr = ADC(2)
#button_pin = Pin(19, Pin.IN, Pin.PULL_UP)
#button_pin = Pin(19, Pin.IN, Pin.PULL_DOWN)

#for i in range(100):
#    print(button_pin.value())
#    sleep(0.5)
#exit()


player = DFPlayer(0, 16, 17, 18)
busy_pin = Pin(18, Pin.IN)
led = Pin("LED", Pin.OUT)

flag=0
debounce=500
delta=0
#button_pin = Pin(19, Pin.IN, Pin.PULL_UP)
button_pin = Pin(19, Pin.IN, Pin.PULL_DOWN)
button_input = Pin(20, Pin.OUT)
button_input.value(0)

count=0

def callback(pin):
    global flag, delta
    if (ticks_ms()-delta) > debounce:
        flag= 1
        delta=ticks_ms()

button_pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

def measure_light(timer):
    read = ldr.read_u16()
    print(read)
    if read < 15000:
        led.on()
        button_input.value(1)
    else:
        led.off()
        button_input.value(0)

timer = Timer(period=250, mode=Timer.PERIODIC, callback=measure_light)

dice_mode = button_pin.value()

while True:
    if flag == 1:
        #print("play")
        if dice_mode:
            player.playTrack(2,randint(1,6))
        else:
            player.playTrack(1,randint(1,7))
        sleep(1)
        while not bool(busy_pin.value()):
            sleep(0.1)
        flag = 0

