# ******************************************
# © 2019 Amar Lokman Some Rights Reserved
# ******************************************

# ---------------------------------------------------------
# ADD MODULES
# ---------------------------------------------------------
import time
import datetime
import RPi.GPIO as GPIO

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
GPIO_RELAY = 20
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GPIO_RELAY,GPIO.OUT, initial=GPIO.HIGH)

count1 = 0
count2 = 0

# ---------------------------------------------------------
# ULTRASONIC SENSOR CONFIGURATION
# ---------------------------------------------------------

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
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
            print ("Measured Distance = %.1f cm" % dist)
            if (count1 == 0) :
                if ( dist > 40 and dist < 220):
                    # Enter Condition
                    # Switch ON bulb and LED
                    GPIO.output (GPIO_RELAY,GPIO.LOW)
                    GPIO.output(GPIO_LED, GPIO.HIGH)
                    count1 += 1
                    count2 = 0
                    print ("Measured Distance = %.1f cm" % dist)
                    print ("---------- State 1 ------------")
                    time.sleep(1)

            else:
                if ( dist > 40 and dist < 220):
                    # Stay Condition
                    GPIO.output (GPIO_RELAY,GPIO.LOW)
                    GPIO.output(GPIO_LED, GPIO.HIGH)
                    count1 += 1
                    print ("Measured Distance = %.1f cm" % dist)
                    print ("---------- State 2 ------------")
                    time.sleep(1)

                else:
                    if (count2 == 0 ) :
                        # Exit Condition
                        # Switch OFF bulb and LED
                        GPIO.output (GPIO_RELAY, GPIO.HIGH)
                        GPIO.output(GPIO_LED, GPIO.LOW)
                        count2 += 1
                        print ("Measured Distance = %.1f cm" % dist)
                        print ("---------- State 3 ------------") 
                        time.sleep(1)

                    else :
                         # Nobody Condition
                         GPIO.output (GPIO_RELAY, GPIO.HIGH)
                         GPIO.output(GPIO_LED, GPIO.LOW)
                         count1 = 0
                         print ("Measured Distance = %.1f cm" % dist)
                         print ("---------- State 4 ------------") 
                         time.sleep(1)
        print ("-------------------------------------------")
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Ending Script Coding")
        GPIO.cleanup()
