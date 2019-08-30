# HCSR-04-Ultrasonic-Sensor

<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/0/8/15569-Ultrasonic_Distance_Sensor_-_HC-SR04-01a.jpg" width="250" />

This is the HC-SR04 ultrasonic ranging sensor. This economical sensor provides 2cm to 400cm of non-contact measurement functionality with a ranging accuracy that can reach up to 3mm. 

# How an Ultarsonic Works
A micro computer sends a electric pulse to ultrasonic sensor via a GPIO Pin. It intern sends out a sound wave, The sound wave bounces off an object and returns to the ultrasonic sensor. The ultra sonic sensor then send a pulse back to the listening GPIO pin of the micro computer, raspberry pi for this example.

# How to determine the distance using an ultrasonic sensor
Sound moves at 1,088 feet per second (332 meters per second). Different air temperatures change the speed of sound but for this article, to keep things simple, will assume sound moves at a constant speed, no matter what the air temperature nor humidity is.

To use a sound wave to determine distance to an object, the sound speed travels will need to be cut in half. The reason for this is one needs to not only consider the time for the sound wave to travel to the object but also to include the time required for the for the sound wave to return to the sensor. For this measurement, consider sound travels at 170 meters per second.

In one second, a sound wave will travel from the ultra sonic sensor to an object 170 meters away and back again. If we wanted to know the amount of time sound travels to an object and back in inches rather than meters, we can apply some simple algebra to determine the formula.

TimeinSeconds * 17000 / 2.5 equals the amount of distance sound traveled in inches.

# Source Code
```
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(1)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance
```
