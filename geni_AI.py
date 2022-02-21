#geni_AI.py

import Mood2Songs
import mechcloud
import Comfy_Ride
import AV_ride # also includes algos



#take readings from Mood, Health Detectors

priority_Mat=mechcloud.getData("Priority_Matrix")
health_Mat=mechcloud.getData("Health_Matrix")
Mood_Mat=mechcloud.getData("Mood_Matrix")
AV_Mat=mechcloud.getData("AV_Matrix") # this includes Route, Battery, temperature etc
Pas_Mat=mechcloud.getData("Passenger_Matrix")  # song preference etc if any

# Optimize Temperature, Route, and Songs accordinly

# analyze Matrix function will analyze the data and update variables
mechcloud.analyzeMat(priority_Mat,health_Mat,Mood_Mat,AV_Mat,Pas_Mat)

#bad mood 

if(AV_ride.badMood(Mood_Mat)):
    Mood2Songs.update(Mood_Mat)


# bad AV condition, be it flat tire etc

if(Comfy_Ride.flat_tire()):
    mechcloud.summon(5)
else(AV_ride.monitorTemp(AV_Mat,Mood_Mat,health_Mat))

if(AV_ride.buttonStatus(3)):
    # FLAT TIRE BUTTON
    mechcloud.summon(5)

if(AV_ride.buttonStatus(2)):
    # SUPPORT BUTTON
    if(AV_ride.buttonStatus(2)):
        # PRess again for interactive talk
        interactive_chat()
    # else Calling Family for Support Call
    else:
        AV_ride.Support("fam",Pas_Mat)

if(AV_ride.buttonStatus(3)):
    # PANIC BUTTON
    mechcloud.summon(4)
    mechcloud.summon(3)
    

