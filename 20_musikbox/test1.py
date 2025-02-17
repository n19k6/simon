from picodfplayer import DFPlayer
from time import sleep
from machine import Pin
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

player = DFPlayer(0, 16, 17, 18)
busy_pin = Pin(18, Pin.IN)
led = Pin("LED", Pin.OUT)

def busy():
    return not bool(busy_pin.value())


player.setVolume(25)

for i in range(1,7):

    #1 = motivation folder 01
    #2 = dice folder 02
    #player.playTrack(2,i)
    player.playTrack(2,randint(1,6))
    print(i)
    sleep(1)
    #sleep(1)
    #led.off()
    #sleep(2)
    #bool barrier = True
    while busy():
        sleep(0.1)
    #    count 
        
        
        
    

