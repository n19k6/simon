"""
created using the following prompt via microsoft copilot:
schreibe mir ein micropython programm für den raspberry pico
welches das lied happy birthday auf einem passiven buzzer auf Pin GP14 abspielt
"""

from machine import Pin, PWM
from time import sleep

# Passiver Buzzer an GP14
buzzer = PWM(Pin(14))
buzzer.duty_u16(30000)  # Lautstärke (0–65535)

def tone(freq, duration):
    if freq == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(freq)
        buzzer.duty_u16(30000)
    sleep(duration)
    buzzer.duty_u16(0)
    sleep(0.02)

# Frequenzen der Noten (in Hz)
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

# Melodie von "Happy Birthday"
melody = [
    (G4, 0.4), (G4, 0.4), (A4, 0.6), (G4, 0.6), (C5, 0.6), (B4, 0.8),
    (G4, 0.4), (G4, 0.4), (A4, 0.6), (G4, 0.6), (D5 := 587, 0.6), (C5, 0.8),
    (G4, 0.4), (G4, 0.4), (G5 := 784, 0.6), (E5 := 659, 0.6), (C5, 0.6), (B4, 0.6), (A4, 0.8),
    (F5 := 698, 0.4), (F5, 0.4), (E5, 0.6), (C5, 0.6), (D5, 0.6), (C5, 1.0)
]

while True:
    for freq, dur in melody:
        tone(freq, dur)
    sleep(2.5)

