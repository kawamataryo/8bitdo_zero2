from evdev import InputDevice, categorize, ecodes
from gpiozero import LED, LEDBarGraph
from time import sleep

gamepad = InputDevice('/dev/input/event0')

print(gamepad)

red = LED(17)
yellow = LED(22)
blue = LED(10)
white = LED(11)

class Btn:
  A = 305
  B = 304
  X = 307
  Y = 306
  R = 309
  L = 308
  START = 313
  SELECT = 312

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY and event.value == 1:
        if event.code == Btn.A:
            print("A")
            yellow.blink(n=1)
        elif event.code == Btn.B:
            print("B")
            red.blink(n=1)
        elif event.code == Btn.X:
            print("X")
            blue.blink(n=1)
        elif event.code == Btn.Y:
            print("Y")
            white.blink(n=1)
        elif event.code == Btn.R:
            print("R")
        elif event.code == Btn.L:
            print("L")
        elif event.code == Btn.START:
            print("START")
        elif event.code == Btn.SELECT:
            print("SELECT")
