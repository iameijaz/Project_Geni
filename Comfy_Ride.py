#  Comfy-Ride.py

# THIS CONSISTS OF TWO SUBPROGRAMS:
# 1. PLOTHOLE DETECTION( SENSORS PLANTED ON THE STRUCTURES ADJACENT TO THE FRONT WHEELS)
# 2. ACTUATORS ( REACT AS PER THE READINGS FROM THE SENSOR READINGS)

import plothole_detector # Takes readings from Kinect and Lidar Sensor
from comfy_actuators import actuatorPush, actuatorPull
import NVH_values # for NVH and gyro values



def flat_tire():
    if(plothole_detected()):
        return True
    elif(AV_ride.buttonStatus(3)):
        # 3rd button is for manual Flat Tire Notify
        return True
    else:
        return False

# Take readings from the plothole detector program

plothole_detector.initialize_pd() # initializes plothole detector

if(plothole_detected()):
    # check if we need to push or pull
    for i in range(0,2):

        if(locate(plothole_matrix(i))==1):
            # we need to push the actuator
            actuatorPush(plothole_matrix(i))
        else:
            actuatorPull(plothole_matrix(i))


if(NVH_values.flat_tire_detection()):
    mechcloud.summon(5) # Status code 5 for Flat Tires
def tire_check(a,b,c,d):
    # check if the values are according to the trained model, else give error to show some faulty tire or flat tire
    pass
