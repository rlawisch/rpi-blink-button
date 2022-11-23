# Raspberry Pi Blink with Button

This example extends the usual Raspberry Pi blink project to control the blinking via a button that toggles it on or off. It is done in Python using the [RPi.GPIO library](https://pypi.org/project/RPi.GPIO/).

## Configuring GPIO pins

There are two GPIO pins involved (for the LED and the button), and they are configured via `LED_PIN` and `BUTTON_PIN` constants, which are given in [BCM pinout](https://pinout.xyz/pinout/).
| Variable | BCM pin | BOARD pin |
| -------- | ------- | --------- |
| BUTTON_PIN | 22 | 15 |
| LED_PIN | 23 | 16 |

## Additional hardware

The LED should be connected to a ~220 Ohms resistor for overcurrent protection. The button requires no additional hardware, as it is configured with an internal pull-down resistor.
