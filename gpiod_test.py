import gpiod

CONSUMER = "led-demo"
c = chip("/dev/gpiochip0")
button = c.get_line(22)
button.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_IN)

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