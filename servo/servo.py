#!/usr/bin/python3
from utils.eightbitdo import EightBitDo
from gpiozero import Servo

# motor
servo = Servo(17)


def main():
    def move_max():
        servo.value = 1

    def move_min():
        servo.value = 0

    def move_middle():
        servo.value = -1

    controller = EightBitDo(
        on_a=move_min,
        on_b=move_middle,
        on_x=move_max,
    )
    controller.listen()


if __name__ == '__main__':
    main()
