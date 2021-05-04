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


class EightBitDo:
    EVENT_FORMAT = "LhBB"
    EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

    def __init__(self,
                 path="/dev/input/js0",
                 action_on_up=lambda: None,
                 action_on_down=lambda: None,
                 action_off_up_or_down=lambda: None,
                 action_on_right=lambda: None,
                 action_on_left=lambda: None,
                 action_off_right_or_left=lambda: None,
                 action_on_y=lambda: None,
                 action_off_y=lambda: None,
                 action_on_x=lambda: None,
                 action_off_x=lambda: None,
                 action_on_a=lambda: None,
                 action_off_a=lambda: None,
                 action_on_b=lambda: None,
                 action_off_b=lambda: None,
                 action_on_r=lambda: None,
                 action_off_r=lambda: None,
                 action_on_l=lambda: None,
                 action_off_l=lambda: None,
                 action_on_start=lambda: None,
                 action_off_start=lambda: None,
                 action_on_select=lambda: None,
                 action_off_select=lambda: None,
                 ):
        self.device_path = path
        self.action_on_up = action_on_up
        self.action_on_down = action_on_down
        self.action_off_up_or_down = action_off_up_or_down
        self.action_on_right = action_on_right
        self.action_on_left = action_on_left
        self.action_off_right_or_left = action_off_right_or_left
        self.action_on_y = action_on_y
        self.action_off_y = action_off_y
        self.action_on_x = action_on_x
        self.action_off_x = action_off_x
        self.action_on_a = action_on_a
        self.action_off_a = action_off_a
        self.action_on_b = action_on_b
        self.action_off_b = action_off_b
        self.action_on_r = action_on_r
        self.action_off_r = action_off_r
        self.action_on_l = action_on_l
        self.action_off_l = action_off_l
        self.action_on_start = action_on_start
        self.action_off_start = action_off_start
        self.action_on_select = action_on_select
        self.action_off_select = action_off_select

    def listen(self):
        with open(self.device_path, "rb") as device:
            while True:
                event = device.read(self.EVENT_SIZE)
                (_time, val, type, num) = struct.unpack(self.EVENT_FORMAT, event)
                code = [val, type, num]

                if code == BtnCode.ON_UP:
                    print("UP_ON")
                    self.action_on_up()
                if code == BtnCode.ON_DOWN:
                    print("DOWN_ON")
                    self.action_on_down()
                if code == BtnCode.OFF_UP_OR_DOWN:
                    print("UP_OR_DOWN_OFF")
                    self.action_off_up_or_down()
                if code == BtnCode.ON_LEFT:
                    print("LEFT_ON")
                    self.action_on_left()
                if code == BtnCode.ON_RIGHT:
                    print("RIGHT_ON")
                    self.action_on_right()
                if code == BtnCode.OFF_RIGHT_OR_LEFT:
                    print("RIGHT_OR_LEFT_OFF")
                    self.action_off_right_or_left()
                if code == BtnCode.ON_A:
                    print("A_ON")
                    self.action_on_a()
                if code == BtnCode.OFF_A:
                    print("A_OFF")
                    self.action_off_a()
                if code == BtnCode.ON_B:
                    print("B_ON")
                    self.action_on_b()
                if code == BtnCode.OFF_B:
                    print("B_OFF")
                    self.action_off_b()
                if code == BtnCode.ON_X:
                    print("X_ON")
                    self.action_on_x()
                if code == BtnCode.OFF_X:
                    print("X_OFF")
                    self.action_off_x()
                if code == BtnCode.ON_Y:
                    print("Y_ON")
                    self.action_on_y()
                if code == BtnCode.OFF_Y:
                    print("Y_OFF")
                    self.action_on_y()
                if code == BtnCode.ON_START:
                    print("START_ON")
                    self.action_on_start()
                if code == BtnCode.OFF_START:
                    print("START_OFF")
                    self.action_off_start()
                if code == BtnCode.ON_SELECT:
                    print("SELECT_ON")
                    self.action_on_select()
                if code == BtnCode.OFF_SELECT:
                    print("SELECT_OFF")
                    self.action_off_select()
                if code == BtnCode.ON_L:
                    print("L_ON")
                    self.action_on_l()
                if code == BtnCode.OFF_L:
                    print("L_OFF")
                    self.action_off_l()
                if code == BtnCode.ON_R:
                    print("R_ON")
                    self.action_on_r()
                if code == BtnCode.OFF_R:
                    print("R_OFF")
                    self.action_off_r()
