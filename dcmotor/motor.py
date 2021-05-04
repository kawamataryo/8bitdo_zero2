#!/usr/bin/python3
from gpiozero import Motor
from utils.eightbitdo import EightBitDo

# motor
motorA = Motor(forward=17, backward=22)
motorB = Motor(forward=10, backward=11)


def main():
    def move_forward():
        motorA.forward()
        motorB.forward()

    def move_backward():
        motorA.backward()
        motorB.backward()

    def stop():
        motorA.stop()
        motorB.stop()

    def move_right():
        motorA.forward(0.1)
        motorB.forward()

    def move_left():
        motorA.forward()
        motorB.forward(0.1)

    controller = EightBitDo(
        on_up=move_forward,
        on_down=move_backward,
        off_up_or_down=stop,
        on_left=move_left,
        on_right=move_right,
        off_right_or_left=stop
    )
    controller.listen()


if __name__ == '__main__':
    main()
