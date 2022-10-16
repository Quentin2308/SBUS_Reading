# pylint: disable=missing-docstring
import sys
from datetime import timedelta
import  gpiod

CONSUMER = "SBUS"
chip = gpiod.Chip("0", gpiod.Chip.OPEN_BY_NUMBER)
c = chip.get_line(22)  # pin 7
c.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

while True:
    if button.event_wait(timedelta(seconds=10)):
        # event_read() is blocking function.
        event = button.event_read()
        if event.event_type == line_event.RISING_EDGE:
            print("rising: ", event.timestamp)
        else:
            print("falling: ", event.timestamp)
    else:
        print("timeout(10s)")
