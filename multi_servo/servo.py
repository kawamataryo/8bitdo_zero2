#!/usr/bin/python

import Adafruit_PCA9685
from utils.eightbitdozero2 import EightBitDoZero2

# servo move
MOVE_MAX = 600
MOVE_MIN = 350

# servo channel
SERVO_1 = 0
SERVO_2 = 4
SERVO_3 = 6

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)


def main():
    def move_max():
        pwm.set_pwm(SERVO_1, 0, 600)
        pwm.set_pwm(SERVO_2, 0, 600)
        pwm.set_pwm(SERVO_3, 0, 600)

    def move_min():
        pwm.set_pwm(SERVO_1, 0, 350)
        pwm.set_pwm(SERVO_2, 0, 350)
        pwm.set_pwm(SERVO_3, 0, 350)

    controller = EightBitDoZero2(
        on_r=move_max,
        on_l=move_min
    )
    controller.listen()


if __name__ == "__main__":
    main()
