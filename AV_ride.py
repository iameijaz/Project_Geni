#AV_ride.py

import mechcloud
import geni_AI
import Comfy_Ride
import Mood2Songs

def badMood(moodMat):
    Mood2Songs(moodMat)

def badAV(AVMat):
    '''
    checking the AV mat '''
    if(AVMat[0]>40):
        return False
    elif(!(Comfy_Ride.tire_check(AVMat[1],AVMat[2],AVMat[3],AVMat[4]))):
        # if this returns a negative number then BAD AV
        return False
    else:
        return True



def call(st_code, Mat):
    # setup using Twilio or similar API
    pass

def notify(st_code, Mat):
    # 
    pass

def alarm(st_code):
    # SIGNAL THE ARDUINO TO BEEP THE BUZZER
    digitalWrite(BUZZER,HIGH)
    delay(500)
    digitalWrite(BUZZER,LOW)


def monitorTemp(AVMat,moodMat,healthMat):
    # USING AN ALGORITHM TO MONITOR THE TEMPERATURE
    pass
