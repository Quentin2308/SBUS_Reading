# GPIO used PD30

import gpiod
import time

chip = gpiod.Chip("/dev/gpiochip0")
line = gpiod.find_line("22")
lines = chip.get_lines([line.offset()])
lines.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_IN)

while True:
    print(lines.get_values())
    time.sleep(1)
    print(lines.get_values())
    time.sleep(1)