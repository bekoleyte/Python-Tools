import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction=digitalio.Direction.OUTPUT

led.value = False
vibration=50
time.sleep(5)

while True:
     led.value = True
     mouse.move(x=vibration)
     led.value = True
     time.sleep(0.5)
     led.value = True
     mouse.move(x=-vibration)
     led.value = True
     time.sleep(0.5)