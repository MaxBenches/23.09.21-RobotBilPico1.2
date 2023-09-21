import machine
import time

gy53 = machine.Pin(19, machine.Pin.IN)

def get_distance():
    while gy53.value() == True:
        pass
    while gy53.value() == False:
        pass
    start_time = time.ticks_us()
    while gy53.value() == True:
        pass
    end_time = time.ticks_us()
    microsec_diff = end_time - start_time
    millimeterdistance = microsec_diff / 10
    distance = millimeterdistance / 10
    print(f"Distance to surface: {distance} cm")
    return distance