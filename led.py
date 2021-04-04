import struct
from gpiozero import LED, LEDBarGraph

# 8BitDo path
device_path = "/dev/input/js0"

# event
EVENT_FORMAT = "LhBB"
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

# btn
class BtnCode:
  Y_ON = [1, 1, 2]
  Y_OFF =  [0, 1, 2]
  X_ON = [1, 1, 3]
  X_OFF = [0, 1, 3]
  A_ON = [1, 1, 1]
  A_OFF = [0, 1, 1]
  B_ON = [1, 1, 0]
  B_OFF = [0, 1, 0]

# led
red = LED(17)
yellow = LED(22)
blue = LED(10)
white = LED(11)

with open(device_path, "rb") as device:
  while True:
    event = device.read(EVENT_SIZE)
    (_time, val, type, num) = struct.unpack(EVENT_FORMAT, event)
    code = [val, type, num]

    if code == BtnCode.Y_ON:
        print("Y ON")
        red.on()
    if code == BtnCode.Y_OFF:
        print("Y ON")
        red.off()
    if code == BtnCode.X_ON:
        print("X ON")
        yellow.on()
    if code == BtnCode.X_OFF:
        print("X OFF")
        yellow.off()
    if code == BtnCode.A_ON:
        print("A ON")
        blue.on()
    if code == BtnCode.A_OFF:
        print("A OFF")
        blue.off()
    if code == BtnCode.B_ON:
        print("B ON")
        white.on()
    if code == BtnCode.B_OFF:
        print("B ON")
        white.off()

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