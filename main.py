from datetime import datetime
import RPi.GPIO as gpio

BUTTON_PIN = 22
LED_PIN = 23

DEBOUNCE_MS = 50
BLINK_PERIOD_MS = 500

last_press_time = datetime.now()
last_toggle_time = datetime.now()
led_state = gpio.LOW


def is_button_pressed() -> bool:
    return gpio.input(BUTTON_PIN) == gpio.HIGH


def is_debouncing() -> bool:
    timediff_ms = (datetime.now() - last_press_time).microseconds / 1000
    return timediff_ms >= DEBOUNCE_MS


def should_toggle_led() -> bool:
    timediff_ms = (datetime.now() - last_toggle_time).microseconds / 1000
    return blinking and timediff_ms >= BLINK_PERIOD_MS / 2


if __name__ == "__main__":
    gpio.setmode(gpio.BCM)
    gpio.setup(BUTTON_PIN, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(LED_PIN, gpio.OUT)

    blinking = True
    released_from_last_press = True

    while True:
        if not is_debouncing():
            if is_button_pressed():
                if released_from_last_press:
                    blinking = not blinking
                    released_from_last_press = False
                last_press_time = datetime.now()
            else:
                released_from_last_press = True

        if should_toggle_led():
            if led_state == gpio.LOW:
                led_state = gpio.HIGH
            else:
                led_state = gpio.LOW

            gpio.output(LED_PIN, led_state)
            last_toggle_time = datetime.now()

gpio.cleanup()
exit()
