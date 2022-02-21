#  Comfy-Ride.py

# THIS CONSISTS OF TWO SUBPROGRAMS:
# 1. PLOTHOLE DETECTION( SENSORS PLANTED ON THE STRUCTURES ADJACENT TO THE FRONT WHEELS)
# 2. ACTUATORS ( REACT AS PER THE READINGS FROM THE SENSOR READINGS)

from plothole_detector import *
from comfy_actuators import actuatorPush, actuatorPull
import NVH_values # for NVH and gyro values


# Take readings from the plothole detector program

initialize_pd() # initializes plothole detector

if(plothole_detected()):
    # check if we need to push or pull
    for i in range(0,2):

        if(locate(plothole_matrix(i))==1):
            # we need to push the actuator
            actuatorPush(plothole_matrix(i))
        else:
            actuatorPull(plothole_matrix(i))

    # send them to the comfy_actuators
retract() # retracts them after the plothole is gone... for all wheels

if(NVH_values.flat_tire_detection()):
    mechcloud.summon(5) # Status code 5 for Flat Tires

