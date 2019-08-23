# ******************************************
# © 2019 Amar Lokman Some Rights Reserved
# ******************************************

# ---------------------------------------------------------
# ADD MODULES
# ---------------------------------------------------------
import time
import datetime
import RPi.GPIO as GPIO
import time

# ---------------------------------------------------------
# GPIO CONFIGURATION
# ---------------------------------------------------------

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO.setwarnings(False)
GPIO_TRIGGER = 17
GPIO_ECHO = 18
GPIO_LED = 16
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT, initial=GPIO.LOW)

# ---------------------------------------------------------
# ULTRASONIC SENSOR CONFIGURATION
# ---------------------------------------------------------

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    # time.sleep(0.00001)
    time.sleep(1)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s) and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# ---------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------

if __name__ ==     '__main__':
    try:
        while True:
            dist = distance()
            print "Distance : ", dist
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Ending Script Coding")
        GPIO.cleanup()
