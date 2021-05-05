from gpiozero import LED
from eightbitdo_zero2 import EightBitDoZero2

# led
red = LED(17)
yellow = LED(22)
blue = LED(10)
white = LED(11)


def main():
    # Initialize controller
    controller = EightBitDoZero2(
        on_y=lambda: red.on(),
        off_y=lambda: red.off(),
        on_x=lambda: yellow.on(),
        off_x=lambda: yellow.off(),
        on_a=lambda: blue.on(),
        off_a=lambda: blue.off(),
        on_b=lambda: white.on(),
        off_b=lambda: white.off(),
    )

    # Start listen
    controller.listen()


if __name__ == "__main__":
    main()
