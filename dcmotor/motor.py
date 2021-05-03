#!/usr/bin/python3
import struct
from gpiozero import Motor
from utils.btncode import BtnCode

# 8BitDo path
device_path = "/dev/input/js0"

# event
EVENT_FORMAT = "LhBB"
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

# motor
motorA = Motor(forward=17, backward=22)
motorB = Motor(forward=10, backward=11)


with open(device_path, "rb") as device:
  while True:
    event = device.read(EVENT_SIZE)
    (_time, val, type, num) = struct.unpack(EVENT_FORMAT, event)
    code = [val, type, num]

    if code == BtnCode.UP_ON:
      print("UP_ON")
      motorA.forward()
      motorB.forward()
    if code == BtnCode.DOWN_ON:
      print("DOWN_ON")
      motorA.backward()
      motorB.backward()
    if code == BtnCode.UP_OR_DOWN_OFF:
      print("UP_OR_DOWN_OFF")
      motorA.stop()
      motorB.stop()
    if code == BtnCode.LEFT_ON:
      print("LEFT_ON")
      motorA.forward(0.1)
      motorB.forward()
    if code == BtnCode.RIGHT_ON:
      print("RIGHT_ON")
      motorA.forward()
      motorB.forward(0.1)
    if code == BtnCode.RIGHT_OR_LEFT_OFF:
      print("RIGHT_OR_LEFT_OFF")
      motorA.stop()
      motorB.stop()
    if code == BtnCode.A_ON:
      print("A_ON")
    if code == BtnCode.A_OFF:
      print("A_OFF")
    if code == BtnCode.B_ON:
      print("B_ON")
    if code == BtnCode.B_OFF:
      print("B_OFF")
    if code == BtnCode.X_ON:
      print("X_ON")
    if code == BtnCode.X_OFF:
      print("X_OFF")
    if code == BtnCode.Y_ON:
      print("Y_ON")
    if code == BtnCode.Y_OFF:
      print("Y_OFF")
    if code == BtnCode.START_ON:
      print("START_ON")
    if code == BtnCode.START_OFF:
      print("START_OFF")
    if code == BtnCode.SELECT_ON:
      print("SELECT_ON")
    if code == BtnCode.SELECT_OFF:
      print("SELECT_OFF")
    if code == BtnCode.L_ON:
      print("L_ON")
    if code == BtnCode.L_OFF:
      print("L_OFF")
    if code == BtnCode.R_ON:
      print("R_ON")
    if code == BtnCode.R_OFF:
      print("R_OFF")
