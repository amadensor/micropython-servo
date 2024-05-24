# Simplified Micropython servo libraries
These are known to work on the Pi Pico.

## servo.py 
Contains the Servo class, which uses the inbuilt PWM duty cycle in nanoseconds to create the correct width pulses for controlling a servo.

* llimit - The shortest a pulse should be
* ulimit - The longest a pulse should be
* pin_num - The pin number that the trigger is connected to
* freq - The frequency that the servo or ESC is expecting to recieve pulses at
* deg_limit - the number of degrees between the shortest and longest pulses

Servo.degrees(n) - Move the servo to n degrees, or run the ESC as if the controller was pressed in a may to make a servo move that far.
It would also be possible to set a degree limit of 100 and use this as the percentage of throttle on an ESC.

## pwmtimer.py
The contains the PwmTimer class which uses interrupts to calculate the length of a pulse in nanoseconds.   This is very useful for reading pulses intended for servos.
This allows timing the pulses very accurately without polling the pin or worring about other processing affecting the polling rate.

* PwmTimer(n) - Begin timing pulses on pin n.
* PwmTimer.pulse - the length of the most recent pulse
