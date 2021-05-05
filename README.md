# 8bitdo zero2

Python code to use the [8bitdo zero2](https://www.8bitdo.com/zero2/) controller with a Raspberry Pi.

<img src="https://i.gyazo.com/7fee2bfe9c81504cda3ec549eb56601f.jpg)" style="max-width: 450px">

# How to use

## Installation


```bash
$ pip install eightbitdo-zero2 
```
## Usage example

```python
from gpiozero import LED
from eightbitdo_zero2 import EightBitDoZero2

# led
red = LED(17)
blue = LED(10)


def main():
    # Initialize controller
    controller = EightBitDoZero2(
        on_y=red.on,
        off_y=red.off,
        on_a=blue.on,
        off_a=blue.off,
    )

    # Start listen
    controller.listen()


if __name__ == "__main__":
    main()
```

There are more example code in [examples](https://github.com/kawamataryo/8bitdo_zero2/tree/master/examples).

## Options

Controller initialize options.

|name|type|default|detail|
|---|---|---|---|
|device_path|string|"/dev/input/js0"|File path to which device is connected.|
|debug|boolean|False|Debug mode setting. When True, The entered command is displayed on STDOUT.|
|on_<button_name>|function|lambda: None|Action when the button is pressed.|
|off_<button_name>|function|lambda: None|Action when the button is Released.|
 
# License

This software is released under the MIT License, see LICENSE.

