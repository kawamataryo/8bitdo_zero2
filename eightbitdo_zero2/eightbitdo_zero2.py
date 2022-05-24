import struct


class BtnCode:
    # cross key
    ON_UP = [-32767, 2, 1]
    ON_DOWN = [32767, 2, 1]
    OFF_UP_OR_DOWN = [0, 2, 1]
    ON_RIGHT = [32767, 2, 0]
    ON_LEFT = [-32767, 2, 0]
    OFF_RIGHT_OR_LEFT = [0, 2, 0]

    # btn
    ON_Y = [1, 1, 2]
    OFF_Y = [0, 1, 2]
    ON_X = [1, 1, 3]
    OFF_X = [0, 1, 3]
    ON_A = [1, 1, 1]
    OFF_A = [0, 1, 1]
    ON_B = [1, 1, 0]
    OFF_B = [0, 1, 0]

    ON_R = [1, 1, 5]
    OFF_R = [0, 1, 5]
    ON_L = [1, 1, 4]
    OFF_L = [0, 1, 4]

    ON_START = [1, 1, 9]
    OFF_START = [0, 1, 9]
    ON_SELECT = [1, 1, 8]
    OFF_SELECT = [0, 1, 8]


class EightBitDoZero2:
    EVENT_FORMAT = "LhBB"
    EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

    def __init__(self,
                 device_path="/dev/input/js0",
                 debug=False,
                 on_up=lambda: None,
                 on_down=lambda: None,
                 off_up_or_down=lambda: None,
                 on_right=lambda: None,
                 on_left=lambda: None,
                 off_right_or_left=lambda: None,
                 on_y=lambda: None,
                 off_y=lambda: None,
                 on_x=lambda: None,
                 off_x=lambda: None,
                 on_a=lambda: None,
                 off_a=lambda: None,
                 on_b=lambda: None,
                 off_b=lambda: None,
                 on_r=lambda: None,
                 off_r=lambda: None,
                 on_l=lambda: None,
                 off_l=lambda: None,
                 on_start=lambda: None,
                 off_start=lambda: None,
                 on_select=lambda: None,
                 off_select=lambda: None,
                 ):
        self.device_path = device_path
        self.debug = debug
        self.on_up = on_up
        self.on_down = on_down
        self.off_up_or_down = off_up_or_down
        self.on_right = on_right
        self.on_left = on_left
        self.off_right_or_left = off_right_or_left
        self.on_y = on_y
        self.off_y = off_y
        self.on_x = on_x
        self.off_x = off_x
        self.on_a = on_a
        self.off_a = off_a
        self.on_b = on_b
        self.off_b = off_b
        self.on_r = on_r
        self.off_r = off_r
        self.on_l = on_l
        self.off_l = off_l
        self.on_start = on_start
        self.off_start = off_start
        self.on_select = on_select
        self.off_select = off_select

    def listen(self):
        with open(self.device_path, "rb") as device:
            while True:
                event = device.read(self.EVENT_SIZE)
                (_time, val, type, num) = struct.unpack(self.EVENT_FORMAT, event)
                code = [val, type, num]

                if code == BtnCode.ON_UP:
                    if self.debug:
                        print("UP_ON")
                    self.on_up()
                if code == BtnCode.ON_DOWN:
                    if self.debug:
                        print("DOWN_ON")
                    self.on_down()
                if code == BtnCode.OFF_UP_OR_DOWN:
                    if self.debug:
                        print("UP_OR_DOWN_OFF")
                    self.off_up_or_down()
                if code == BtnCode.ON_LEFT:
                    if self.debug:
                        print("LEFT_ON")
                    self.on_left()
                if code == BtnCode.ON_RIGHT:
                    if self.debug:
                        print("RIGHT_ON")
                    self.on_right()
                if code == BtnCode.OFF_RIGHT_OR_LEFT:
                    if self.debug:
                        print("RIGHT_OR_LEFT_OFF")
                    self.off_right_or_left()
                if code == BtnCode.ON_A:
                    if self.debug:
                        print("A_ON")
                    self.on_a()
                if code == BtnCode.OFF_A:
                    if self.debug:
                        print("A_OFF")
                    self.off_a()
                if code == BtnCode.ON_B:
                    if self.debug:
                        print("B_ON")
                    self.on_b()
                if code == BtnCode.OFF_B:
                    if self.debug:
                        print("B_OFF")
                    self.off_b()
                if code == BtnCode.ON_X:
                    if self.debug:
                        print("X_ON")
                    self.on_x()
                if code == BtnCode.OFF_X:
                    if self.debug:
                        print("X_OFF")
                    self.off_x()
                if code == BtnCode.ON_Y:
                    if self.debug:
                        print("Y_ON")
                    self.on_y()
                if code == BtnCode.OFF_Y:
                    if self.debug:
                        print("Y_OFF")
                    self.off_y()
                if code == BtnCode.ON_START:
                    if self.debug:
                        print("START_ON")
                    self.on_start()
                if code == BtnCode.OFF_START:
                    if self.debug:
                        print("START_OFF")
                    self.off_start()
                if code == BtnCode.ON_SELECT:
                    if self.debug:
                        print("SELECT_ON")
                    self.on_select()
                if code == BtnCode.OFF_SELECT:
                    if self.debug:
                        print("SELECT_OFF")
                    self.off_select()
                if code == BtnCode.ON_L:
                    if self.debug:
                        print("L_ON")
                    self.on_l()
                if code == BtnCode.OFF_L:
                    if self.debug:
                        print("L_OFF")
                    self.off_l()
                if code == BtnCode.ON_R:
                    if self.debug:
                        print("R_ON")
                    self.on_r()
                if code == BtnCode.OFF_R:
                    if self.debug:
                        print("R_OFF")
                    self.off_r()
