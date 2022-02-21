#mechcloud.py

import geni_AI
import Comfy_Ride
import requests
import urllib.request
THINGSPEAK_CHANNEL_NAME = ""
REQUEST_LINK = "https://thingspeak.com/channels/" +THINGSPEAK_CHANNEL_NAME + "/field/1"

global cloud_data

def getData(paramet):

    if(paramet=="Priority_Matrix"):
        return Priority_Matrix
    elif(paramet=="Health_Matrix"):
        return Health_Matrix
    elif(paramet=="Mood_Matrix"):
        return Mood_Matrix
    elif(paramet=="AV_Matrix"):
        return AV_Matrix
    elif(paramet=="Passenger_Matrix"):
        return Passenger_Matrix
    else:
        return 0

def fetch_data():
    cloud_data=requests.get(REQUEST_LINK)
    cloud_data=cloud_data.json()['feeds'][-1]['field1']
    return cloud_data

def mechcloud_init():
    '''
    THIS METHOD WILL INITIALIZE THE MECHCLOUD MODULE BY GETTING PASSENGER'S DATA FROM THE CLOUD, AND THE CREATE THE ESSENTIAL MATRICES 
    WHICH WILL BE THE ESSENTIAL ONES FOR THIS TECHNOLOGY
    
    '''
    # GET PASSENGER DATA FROM THE CLOUD



# FREE SUBSCRIPTION ALLOWS 255 FIELDS, SO WE WILLL DIVIDE THEM EVENLY FOR OUR MATRICES
# FIRST OF ALL WE WILL DECIDE THE ORDER FOR FETCHING AND UPLOADING OUR DATA ON THE CLOUD
# THE FIRST FIELD WILL HAVE ITS FIRST ENTRY FOR THE BATTERY LEVEL
# FOLLOWED BY ENTRIES 1,2,3,4 WILL BE FOR THE EXTERNAL GYROSCOPE OR NVH VALUES FROM THE 4 TYRES
# 
#----------------------------------------
# ENTRY:0 --> BATTERY LEVEL

# ENTRY:1~4 --> TYRES& NVH(GYROSCOPE) VALUES --> FURTHER ANALYZED BY TRAINED ML ALGORITHM FOR FLAT-TIRE DETECTION IN ADVANCE

# NOW THE PASSENGER RELATED DATA
# 4 PASSENGERS ... 6*4=24... 5+24=29... SO FROM ENTRY 5 TILL 29 WE HAVE PASSENGER DATA
# NAME
# AGE
# MEDICAL RECORD --> DISEASE/ISSUE AND SEVERITY LEVEL Like CHOLESTEROL,34,BLOOD PRESSURE(S,D),67 88, AND SO ON
# EMERGENCY CONTACT
# CURRENT_MOOD
# PREFERENCES --> TO MAKE THEIR MOOD BETTER BE IT SONGS OR TEMPERATURE




for i in range(0,256): 
    # RECEIVE THE DATA, AND PUT IT INTO RESPECTIVE MATRICES

    #----------------------------------------
    # ENTRY:0 --> BATTERY LEVEL

    #AV_matrix includes:
    # Battery level & Location
    # 4 tire gyro readings

    # iterate a loop from 0 to 4
    for j in range(0,5):
        AV_Matrix[j]=fetch_data() 
    
    

# ENTRY:1~4 --> TYRES& NVH(GYROSCOPE) VALUES --> FURTHER ANALYZED BY TRAINED ML ALGORITHM FOR FLAT-TIRE DETECTION IN ADVANCE

# NOW THE PASSENGER RELATED DATA

# 4 PASSENGERS ... 6*4=24... 5+24=29... SO FROM ENTRY 5 TILL 29 WE HAVE PASSENGER DATA
# NAME
# AGE
# MEDICAL RECORD --> DISEASE/ISSUE AND SEVERITY LEVEL Like CHOLESTEROL,34,BLOOD PRESSURE(S,D),67 88, AND SO ON
# EMERGENCY CONTACT
# PREFERENCES --> TO MAKE THEIR MOOD BETTER BE IT SONGS OR TEMPERATURE



# NOW TIME FOR 4 PASSENGERS
# Time for counters
#passenger_count=0

# ~ 25 VALUES  5 ONWARDS... 5  TILL 5+24-> 28 ... SO 5 TO 29
for k in range(0,29):
    Passenger_Matrix[p]=fetch_data()
    for p in range(k,k+5)
    #Names
        Passenger_Matrix[p]=fetch_data()
        if(p==k+5):
            Priority_Matrix[prioritycount]=Passenger_Matrix[p]
            prioritycount+=1

    # 5 values... age, medical record, emergency contact, preferences

# time for Mood Matrix # CURRENT_MOOD

# sTARTING FROM 30, AND  UNTIL 30+5=35, SO,  30->34

for k in range(0,5):
    Mood_Matrix[k]=fetch_data()


# TIME FOR HEALTH MATRIX USING BIOSENSORS ON ARDUINO OR SIMILAR BOARD
#~34 -> 39
for k in range(0,5):
    Health_Matrix[k]=fetch_data()



# from 40 until onwards...
# 40 -> IN CASE ANY NOTIFICATION HAS TO BE SENT
# 41 -> STATUS CODE 1 
# 42 -> STATUS CODE 2
# 43 -> STATUS CODE 3
# 44 -> STATUS CODE 4
# 45 -> STATUS CODE 5 --> FLAT TIRE




    # CREATE THE MATRICES
    '''
    THIS INCLUDES
    0. AV_MATRIX
    1. PASSENGER MATRIX
        - THIS WILL INCLUDE AND DECIDE THEIR NAMES, AND LOCATION IN THE CAR
    2. MOOD MATRIX
    3. HEALTH MATRIX
    
    '''

# Get status codes 
# and Respond Accordingly

#THE OTHER MODULES WILL CALL THE SUMMON METHOD AND THEN THE STATUS CODES AND RESPONSES WILL BE GIVEN ACCORDINLY IN THAT METHOD.


def summon(status_code):

    '''
    THIS FUNCTION WILL RECEIVE A STATUS CODE AND THEN THIS WILL RESPOND ACCORDINLY...

    THIS WILL SEND A NOTIFICATION TO THE FAMILY FOR ALL OF THE 5 STATUS CODES HERE

    '''
    AV_ride.notify(status_code,Passenger_Matrix)

    # Status_Code=1 
    if(status_code==1):
        #Kids and/or Someone else is Peeking outside the window
        # This will activate the Window Proximity Alarm
        
        #Print Status Code
        print(f"Status Code: {status_code}")
        

        #Print Message 

        print("Window Proximity Alarm")


        #Send Notification
        # GMAIL? or just cloud?




        #Respond
        

        # Start the Alarm 
        AV_ride.alarm(status_code)

        '''
        CALL THE ALARM FUNCTION FROM AV_RIDE OR SIMILAR MODULE
        AND TURN THE RESPECTIVE BOOLEAN VARIABLE
        '''

    # Status_Code=2
    elif(status_code==2):
        # What is this status Code
        # and What is the Response
        
        # Safety Belt & SOPs-> Alarm
        
        #Print Status Code
        print(f"Status Code: {status_code}")
        

        #Print Message 

        print("Safety Belt & SOPs Alarm")


        #Send Notification
        # GMAIL? or just cloud?



        #Respond

        # START ALARM FOR SAFETY BELT AND SOPS
        '''
        CALL THE ALARM FUNCTION FROM AV_RIDE OR SIMILAR MODULE
        '''
        AV_ride.alarm(status_code)
        # IF SEAT BELT ARE FASTENED OR MASKS WORN, THEN TURN THE RESPECTIVE BOOLEAN FALSE


        # 

    elif(status_code==3):
        # What is this status Code
        # and What is the Response
        # Critical Health -> Summon Ambulance+Contact Medical Experts

        
        #Print Status Code
        print(f"Status Code: {status_code}")
        

        #Print Message 

        print("Critical Health Alarm")


        #Send Notification
        # GMAIL? or just cloud?




        #Respond
        AV_ride.call(status_code,Passenger_Matrix)

        # CALL Medic WITH PARAMETERS OF GPS LOCATION AND Critical Health

        # 

    elif(status_code==4):
        # What is this status Code
        # and What is the Response
        # 4 : Battery isseus -> to call an AV expert
        
        #Print Status Code
        print(f"Status Code: {status_code}")
        

        #Print Message 

        print("Battery Issues")


        #Send Notification
        # GMAIL? or just cloud?




        #Respond

        # CALL AV-EXPERT WITH PARAMETERS OF BATTERY  & GPS LOCATION 
        AV_ride.call(status_code,AV_Matrix)
        # 

    elif(status_code==5):
        # What is this status Code
        # and What is the Response
        # Flat tires -> to call an AV expert
        
        #Print Status Code
        print(f"Status Code: {status_code}")
        

        #Print Message 

        print("Flat Tires")


        #Send Notification
        # GMAIL? or just cloud?




        #Respond

        # CALL AV-EXPERT WITH PARAMETERS OF GPS LOCATION AND BATTERY
        AV_ride.call(status_code,AV_Matrix)
        # 





'''
# Status Codes:

5 : Flat tires -> to call an AV expert
4 : Battery isseus -> to call an AV expert
3 : Critical Health -> Summon Ambulance+Contact Medical Experts
2 : Safety Belt & SOPs-> Alarm
1 : Kids+Peeking Window -> Alarm
'''




# update the Matrices


def analyzeMat(priority_Mat,health_Mat,Mood_Mat,AV_Mat,Pass_Mat):
    # the algorithm ...
    pass
