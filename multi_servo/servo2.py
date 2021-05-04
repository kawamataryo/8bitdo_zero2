#!/usr/bin/python

import Adafruit_PCA9685
import time
import struct
from utils.btncode import BtnCode

# 8BitDo path
device_path = "/dev/input/js0"

# event
EVENT_FORMAT = "LhBB"
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

# servo move
MOVE_MAX = 600
MOVE_MIN = 350

# servo channel
SERVO_1 = 0
SERVO_2 = 4
SERVO_3 = 6

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)

with open(device_path, "rb") as device:
  while True:
    event = device.read(EVENT_SIZE)
    (_time, val, type, num) = struct.unpack(EVENT_FORMAT, event)
    code = [val, type, num]

    if code == BtnCode.R_ON:
        print("R ON")
        # pwm.set_pwm(SERVO_3, 0, 350)
        # time.sleep(1)
        # pwm.set_pwm(SERVO_2, 0, 350)
        # time.sleep(1)
        pwm.set_pwm(SERVO_1, 0, 600)

    if code == BtnCode.L_ON:
        print("L ON")
        # pwm.set_pwm(SERVO_3, 0, 600)
        # time.sleep(1)
        # pwm.set_pwm(SERVO_2, 0, 600)
        # time.sleep(1)
        pwm.set_pwm(SERVO_1, 0, 350)