#!/usr/bin/python3
import struct
from gpiozero import Motor

# 8BitDo btn code
class BtnCode:
  UP_ON = [-32767, 2, 1]
  DOWN_ON = [32767, 2, 1]
  UP_OR_DOWN_OFF = [0, 2, 1]
  RIGHT_ON = [32767, 2, 0]
  LEFT_ON = [-32767, 2, 0]
  RIGHT_OR_LEFT_OFF = [ 0, 2, 0 ]
  Y_ON = [ 1, 1, 2 ]
  Y_OFF =  [ 0, 1, 2 ]
  X_ON = [1, 1, 3]
  X_OFF = [0, 1, 3]
  A_ON = [1, 1, 1]
  A_OFF = [0, 1, 1]
  B_ON = [1, 1, 0]
  B_OFF = [0, 1, 0]
  R_ON = [1, 1, 5]
  R_OFF = [0, 1, 5]
  L_ON = [1, 1, 4]
  L_OFF = [0, 1, 4]
  START_ON = [1, 1, 9]
  START_OFF = [0, 1, 9]
  SELECT_ON = [1, 1, 8]
  SELECT_OFF = [0, 1, 8]

# 8BitDo path
device_path = "/dev/input/js0"

# event
EVENT_FORMAT = "LhBB"
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

# motor
motorA = Motor(forward=17, backward=18)
motorB = Motor(forward=22, backward=23)


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
      motorA.backward()
      motorB.forward()
    if code == BtnCode.RIGHT_ON:
      print("RIGHT_ON")
      motorA.forward()
      motorB.backward()
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
