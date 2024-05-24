"""Servo controller for MicroPython"""
class Servo:

    def __init__(self, llimit=500000, ulimit=2500000, pin_num=16, freq=50, deg_limit=180):
        """Initialize values to reasonable defailts and create PWN object"""
        self.llimit=llimit
        self.ulimit=ulimit
        self.pin_num=pin_num
        self.freq=freq
        self.deg_limit=deg_limit
        self.pin=machine.PWM(machine.Pin(self.pin_num))
        self.pin.freq(self.freq)
    def degrees(self,deg):
        """Move servo to select degrees angle"""
        nano_secs=int(self.llimit+((self.ulimit-self.llimit)*(deg/self.deg_limit)))
        self.pin.duty_ns(nano_secs)
