import gpiod

CONSUMER = "led-demo"
chip = gpiod.Chip("/dev/gpiochip0", gpiod.Chip.OPEN_BY_NUMBER)

button = chip.get_line(22)  # pin 7
button.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_IN)

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