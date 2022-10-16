import gpiod

CONSUMER = "led-demo"
chip = gpiod.Chip("/dev/gpiochip0", gpiod.Chip.OPEN_BY_NUMBER)

button = chip.get_line(22)  # pin 7
button.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_IN)

try:
  while True:
    led.set_value(button.get_value())
finally:
  led.set_value(0)
  led.release()
  button.release()