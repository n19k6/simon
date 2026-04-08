import machine
import utime

led_external = machine.Pin(3, machine.Pin.OUT)
button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led_external.value(1)
        utime.sleep(2)
    led_external.value(0)

