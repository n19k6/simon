import machine
import utime
import urandom

led_red = machine.Pin(3, machine.Pin.OUT)
#led_amber = machine.Pin(4, machine.Pin.OUT)
#led_green = machine.Pin(5, machine.Pin.OUT)

button_yellow = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
button_green = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
#buzzer = machine.Pin(15, machine.Pin.OUT)

pressed = False
fastest_button = None

def button_handler(pin):
    global pressed
    if not pressed:
        pressed=True
        global fastest_button
        fastest_button = pin
        
led_red.value(1)
utime.sleep(urandom.uniform(5, 10))
led_red.value(0)

timer_start = utime.ticks_ms()
button_yellow.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
button_green.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)

while fastest_button is None:
    utime.sleep(1)
if fastest_button is button_yellow:
    print("Left Player wins!")
elif fastest_button is button_green:
    print("Right Player wins!")

