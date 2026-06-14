from machine import Pin, I2C, PWM
import time
import ssd1306

# ============================================================
# PIN CONFIG
# ============================================================
LED_PINS = [2, 3, 4, 5]           # Blue, Red, Yellow, Green
BUTTON_PINS = [10, 11, 12, 13]    # Blue, Red, Yellow, Green
BUZZER_PIN = 14                   # Passive buzzer
ALARM_PIN = 15                    # Active buzzer

WIDTH = 128
HEIGHT = 64

# OLED I2C wiring
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# ============================================================
# GAME SETTINGS
# ============================================================
START_SECONDS = 5 * 60     # 5 minutes per player
INCREMENT_SECONDS = 0       # set to 2, 3, etc. if you want increment

# ============================================================
# HARDWARE SETUP
# ============================================================
leds = [Pin(p, Pin.OUT) for p in LED_PINS]
for led in leds:
    led.off()

buttons = [Pin(p, Pin.IN, Pin.PULL_UP) for p in BUTTON_PINS]

passive_buzzer = PWM(Pin(BUZZER_PIN))
passive_buzzer.duty_u16(0)

alarm_buzzer = Pin(ALARM_PIN, Pin.OUT)
alarm_buzzer.off()

# Button order:
# 0 = Blue, 1 = Red, 2 = Yellow, 3 = Green
btn_blue = buttons[0]
btn_red = buttons[1]
btn_yellow = buttons[2]
btn_green = buttons[3]

# LED order:
# 0 = Blue, 1 = Red, 2 = Yellow, 3 = Green
led_blue = leds[0]
led_red = leds[1]
led_yellow = leds[2]
led_green = leds[3]

# ============================================================
# HELPERS
# ============================================================
def format_time(ms):
    if ms < 0:
        ms = 0
    total_seconds = ms // 1000
    mm = total_seconds // 60
    ss = total_seconds % 60
    return "{:02d}:{:02d}".format(mm, ss)

def beep(freq=1200, ms=50):
    passive_buzzer.freq(freq)
    passive_buzzer.duty_u16(30000)
    time.sleep_ms(ms)
    passive_buzzer.duty_u16(0)

def error_beep():
    beep(300, 80)
    time.sleep_ms(50)
    beep(300, 80)

def alarm_beep():
    # Active buzzer alarm
    for _ in range(20):
        alarm_buzzer.on()
        time.sleep_ms(100)
        alarm_buzzer.off()
        time.sleep_ms(100)

class DebouncedButton:
    def __init__(self, pin, debounce_ms=50):
        self.pin = pin
        self.debounce_ms = debounce_ms
        self.last_raw = pin.value()
        self.stable = self.last_raw
        self.last_change = time.ticks_ms()
        self.pressed_event = False

    def update(self, now):
        raw = self.pin.value()

        if raw != self.last_raw:
            self.last_raw = raw
            self.last_change = now

        if time.ticks_diff(now, self.last_change) > self.debounce_ms:
            if raw != self.stable:
                self.stable = raw
                if self.stable == 0:
                    self.pressed_event = True

    def pressed(self):
        if self.pressed_event:
            self.pressed_event = False
            return True
        return False

# ============================================================
# GAME STATE
# ============================================================
remaining = [START_SECONDS * 1000, START_SECONDS * 1000]  # [Blue, Green]
turn = 0           # 0 = Blue, 1 = Green
running = False
game_over = False
last_tick = time.ticks_ms()

dbuttons = [DebouncedButton(pin) for pin in buttons]

def set_leds():
    # Blue LED for blue player's turn, Green LED for green player's turn
    # Yellow LED for paused, Red LED for game over
    for led in leds:
        led.off()

    if game_over:
        led_red.on()
    elif not running:
        led_yellow.on()
    else:
        if turn == 0:
            led_blue.on()
        else:
            led_green.on()

def draw():
    oled.fill(0)
    oled.text("CHESS CLOCK", 20, 0)

    oled.text("BLUE :", 0, 16)
    oled.text(format_time(remaining[0]), 54, 16)

    oled.text("GREEN:", 0, 32)
    oled.text(format_time(remaining[1]), 54, 32)

    if game_over:
        if remaining[0] <= 0:
            oled.text("BLUE TIME UP", 0, 48)
        else:
            oled.text("GREEN TIME UP", 0, 48)
    elif running:
        oled.text("RUNNING", 0, 48)
        oled.text("B" if turn == 0 else "G", 96, 48)
    else:
        oled.text("PAUSED", 0, 48)

    oled.show()

def reset_clock():
    global remaining, turn, running, game_over, last_tick
    remaining = [START_SECONDS * 1000, START_SECONDS * 1000]
    turn = 0
    running = False
    game_over = False
    last_tick = time.ticks_ms()
    set_leds()
    draw()

def switch_turn():
    global turn, last_tick

    # Add increment to the player who just moved
    if INCREMENT_SECONDS > 0:
        remaining[turn] += INCREMENT_SECONDS * 1000

    turn = 1 - turn
    last_tick = time.ticks_ms()
    set_leds()
    beep(1200, 40)

def update_clock(now):
    global running, game_over, last_tick

    if not running or game_over:
        return

    elapsed = time.ticks_diff(now, last_tick)
    if elapsed <= 0:
        return

    remaining[turn] -= elapsed
    last_tick = now

    if remaining[turn] <= 0:
        remaining[turn] = 0
        running = False
        game_over = True
        set_leds()
        draw()
        alarm_beep()

# ============================================================
# STARTUP SCREEN
# ============================================================
reset_clock()
oled.fill(0)
oled.text("CHESS CLOCK", 20, 8)
oled.text("Y: Start/Pause", 0, 28)
oled.text("R: Reset", 0, 40)
oled.text("B/G: Move", 0, 52)
oled.show()
time.sleep_ms(1200)
draw()

# ============================================================
# MAIN LOOP
# ============================================================
while True:
    now = time.ticks_ms()

    # Update all buttons
    for b in dbuttons:
        b.update(now)

    # RED = reset
    if dbuttons[1].pressed():
        reset_clock()
        beep(1500, 50)

    # YELLOW = start / pause / resume
    if dbuttons[2].pressed():
        if game_over:
            reset_clock()
        else:
            running = not running
            last_tick = time.ticks_ms()
            set_leds()
            beep(1000, 40)
            draw()

    # BLUE button = blue player's move
    if dbuttons[0].pressed():
        if running and not game_over and turn == 0:
            switch_turn()
            draw()
        elif not running and not game_over:
            # Optional: allow selecting blue turn while paused
            turn = 0
            set_leds()
            draw()
            beep(900, 30)
        else:
            error_beep()

    # GREEN button = green player's move
    if dbuttons[3].pressed():
        if running and not game_over and turn == 1:
            switch_turn()
            draw()
        elif not running and not game_over:
            # Optional: allow selecting green turn while paused
            turn = 1
            set_leds()
            draw()
            beep(900, 30)
        else:
            error_beep()

    update_clock(now)
    draw()
    time.sleep_ms(20)
