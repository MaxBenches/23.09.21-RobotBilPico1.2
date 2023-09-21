import motor
import gy53

def follow_wall():

    """ Standard speed definitions """
    speed = 0.5  # for motor module
    speedL = 0.5  # left motor
    speedR = 0.5  # right motor


    def dutycycleLEFT(speedL):
        motor.pwm_motor1.duty_u16(int(65536 * speedL))  # Left Speed

    def dutycycleRIGHT(speedR):
        motor.pwm_motor2.duty_u16(int(65536 * speedR))  # Right Speed

    while True:
        motor.forward(speed)
        distance = gy53.get_distance()
        if distance in range(15, 29): # drej til mod væg
            #Up PWM på motor mod væg
            """ SÆT PWM OP PÅ VENSTRE HJUL HER """
            speedL = 0.9
            dutycycleLEFT(speedL)
            IN1.on()
            IN3.on()
        elif distance in range(1, 9): # drej væk fra væg
            # Up PWM på motor mod væg
            """ SÆT PWM OP PÅ VENSTRE HJUL HER """
            speedR = 0.9
            dutycycleRIGHT(speedR)
            IN1.on()
            IN3.on()
        elif distance in range(10, 15):
            # PWM standard fremad
            speedL = 0.5
            speedR = 0.5
            dutycycleLEFT(speedL)
            dutycycleRIGHT(speedR)
            IN1.on()
            IN3.on()
        elif distance in range(30, 200): # drej højre på egen akse når væg er langt væk
            IN1.on()
            IN4.on()