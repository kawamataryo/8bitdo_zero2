#!/usr/bin/python3
import struct
from utils.btncode import BtnCode
from gpiozero import Servo

# 8BitDo path
device_path = "/dev/input/js0"

# event
EVENT_FORMAT = "LhBB"
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

# motor
servo = Servo(17)

with open(device_path, "rb") as device:
  while True:
    event = device.read(EVENT_SIZE)
    (_time, val, type, num) = struct.unpack(EVENT_FORMAT, event)
    code = [val, type, num]

    if code == BtnCode.A_ON:
      print("A")
      servo.value = -1
    if code == BtnCode.B_ON:
      print("B")
      servo.value = -0.5
    if code == BtnCode.Y_ON:
      print("Y")
      servo.value = 1
    if code == BtnCode.X_ON:
      print("X")
      servo.value = 0.5