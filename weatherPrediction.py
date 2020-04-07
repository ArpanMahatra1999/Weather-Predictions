from sense_hat import SenseHat
import time
from time import asctime

sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    bg = [0, 0, 100]
    tc = [200, 200, 0]

    msg = "Temperature = {0} Pressure = {1} Humidity = {2} .".format(t, p, h)
    sense.show_message(msg, scroll_speed=0.1, text_colour=tc, back_colour=bg)

    time.sleep(4)
    log = open('weather.txt', "a")
    now = str(asctime())
    log.write(now + '' + msg + '\n')
    print(msg)
    log.close()
    time.sleep(5)