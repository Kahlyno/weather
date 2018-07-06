import RPi.GPIO as LED_Light
import time
LED_Light.setmode(LED_Light.BOARD)
LED_Light.setup(7, LED_Light.OUT)
#loop through 50 times, on/off for 10 seconds.
for i in range(1,100):
    LED_Light.output(7, True)
    time.sleep(0.1)
    LED_Light.output(7, False)
    time.sleep(0.1)

LED_Light.cleanup()
