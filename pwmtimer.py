import machine
import utime

class PwmTimer:
    def __init__(self, pin_num):
        self.time_pin=machine.Pin(pin_num,mode=machine.Pin.IN)
        self.st_time=0
        self.pulse=0
        self.time_pin.irq(trigger=machine.Pin.IRQ_RISING,handler=self.pulse_start)

    def pulse_start(self, p):
        self.st_time=utime.ticks_us()
        self.time_pin.irq(trigger=machine.Pin.IRQ_FALLING,handler=self.pulse_end)


    def pulse_end(self, p):
        self.pulse=utime.ticks_us()-self.st_time
        self.time_pin.irq(trigger=machine.Pin.IRQ_RISING,handler=self.pulse_start)

