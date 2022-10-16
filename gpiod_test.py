# pylint: disable=missing-docstring
import sys
from datetime import timedelta
import gpiod


BUTTON_CHIP = 0
BUTTON_LINE_OFFSET = 22

c = chip(BUTTON_CHIP)
button = c.get_line(BUTTON_LINE_OFFSET)

config = gpiod.line_request()
config.consumer = "Button"
config.request_type = gpiod.LINE_REQ_DIR_OUT

button.request(config)

print("event fd: ", button.event_get_fd())

while True:
    if button.event_wait(10):
        # event_read() is blocking function.
        event = button.event_read()
        if event.event_type == line_event.RISING_EDGE:
            print("rising: ", event.timestamp)
        else:
            print("falling: ", event.timestamp)
    else:
        print("timeout(10s)")
