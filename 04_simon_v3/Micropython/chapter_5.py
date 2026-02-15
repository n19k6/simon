import machine
import utime
import _thread

led_red = machine.Pin(3, machine.Pin.OUT)
led_amber = machine.Pin(4, machine.Pin.OUT)
led_green = machine.Pin(5, machine.Pin.OUT)

button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
buzzer = machine.Pin(15, machine.Pin.OUT)

global button_pressed
global button_count
button_pressed = False
button_count = 0

def button_reader_thread():
    global button_pressed
    global button_count
    while True:
        if button.value() == 0:
            button_pressed = True
            print("button pressed [" + str(button_count) + "]")
            button_count = button_count + 1
        utime.sleep(0.01)
        
_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:
        led_red.value(1)
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        global button_pressed
        global button_count
        button_pressed = False
        button_count = 0
        print("button status deleted")
    led_red.value(1)
    utime.sleep(5)
    led_amber.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(5)
    led_amber.value(0)
    
    
    

