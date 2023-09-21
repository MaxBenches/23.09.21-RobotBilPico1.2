import machine

""" PIN ASSIGNMENTS """
ir = machine.Pin(6, machine.Pin.IN)

def get_QRE1113_val():
    get_sensor = ir.value()
    if get_sensor == 0:
        return "White"
    else:
        return "Black"