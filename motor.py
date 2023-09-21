import machine


""" PIN ASSIGNMENTS """
# H-Bridge Pins
IN1 = machine.Pin(0, machine.Pin.OUT)   # IN1 on = FORWARD
IN2 = machine.Pin(1, machine.Pin.OUT)   # IN2 on = BACKWARD
IN3 = machine.Pin(2, machine.Pin.OUT)   # IN3 on = FORWARD
IN4 = machine.Pin(3, machine.Pin.OUT)   # IN4 on = BACKWARD

# PWM Pin
pwm_motor1 = machine.PWM(machine.Pin(4))  #EN-A
pwm_motor2 = machine.PWM(machine.Pin(5))  #EN-B

# PWM Frequency
pwm_motor1.freq(1000)
pwm_motor2.freq(1000)

""" FUNCTIONS """
# Stops both motors
def stop_motors():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()

def forward(speed):
    IN1.on()
    IN2.off()
    IN3.on()
    IN4.off()
    pwm_motor1.duty_u16(int(65536 * speed))     # Left Speed
    pwm_motor2.duty_u16(int(65536 * speed))     # Right Speed

def backward(speed):
    IN1.off()
    IN2.on()
    IN3.off()
    IN4.on()
    pwm_motor1.duty_u16(int(65536 * speed))     # Left Speed
    pwm_motor2.duty_u16(int(65536 * speed))     # Right Speed