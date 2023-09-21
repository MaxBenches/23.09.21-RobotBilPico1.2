import qre1113
import motor
import machine
import gy53
import time

# H-Bridge Pins
IN1 = machine.Pin(0, machine.Pin.OUT)   # IN1 on = FORWARD
IN2 = machine.Pin(1, machine.Pin.OUT)   # IN2 on = BACKWARD
IN3 = machine.Pin(2, machine.Pin.OUT)   # IN3 on = FORWARD
IN4 = machine.Pin(3, machine.Pin.OUT)   # IN4 on = BACKWARD

speed = 13000


def stopVedSort(qre_val):
    if qre_val == 1:
        time.sleep(1)
        motor.stop_motors()


def push_crate():
    while True:
        qre_val = qre1113.get_QRE1113_val()
        print(qre_val)
        # bruger for loop til at stille og roligt scanne i stedet
        for angle in range(0, 360, 10):
            distance = gy53.get_distance()
            IN2.off()
            IN3.off()
            IN4.off()
            IN1.on()
            if distance >= 100:
                pass
            elif distance <= 100:  # her er jeg usikker på hvordan vi får den tilbage til start position
                motor.forward(speed)
                stopVedSort(qre_val)
                time.sleep(1)
                IN2.on()
                IN4.on()
                time.sleep(2)
                IN2.off()
                IN3.off()
                IN4.off()
                IN1.on()
                time.sleep(2)
