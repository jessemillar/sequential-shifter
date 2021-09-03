# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
import analogio
import usb_hid

from adafruit_hid.gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

# Create some buttons. The physical buttons are connected
# to ground on one side and these and these pins on the other.
button_pins = (board.GP0, board.GP1, board.GP2, board.GP3)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
gamepad_buttons = (1, 2, 8, 15)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    # button.pull = digitalio.Pull.UP

# Connect an analog two-axis joystick to A4 and A5.
#ax = analogio.AnalogIn(board.A4)
#ay = analogio.AnalogIn(board.A5)

# Equivalent of Arduino's map() function.
#def range_map(x, in_min, in_max, out_min, out_max):
#    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    # Buttons are grounded when pressed (.value = False).
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            #print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            #print(" press", gamepad_button_num, end="")