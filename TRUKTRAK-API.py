################ IMPORT THE NEEDED LIBRARYS
import requests
import xmltodict
import csv
import time
import os
############### Connect to the API to get the token
url = "https://ttapi.trutrakpro.co.uk/WSDataProvider.asmx/TTAuthenticate" 
head = {
    "Login": "your login credentials",
    "Password": "your password",
    "SKey":"your secret key"
}
auth_response = requests.post(url, data=head)
response_xml = auth_response
preview = xmltodict.parse(response_xml.content) #### PARSE XML FILE
tokenkey = preview["Root"]["Authenticated"]["Token"] #### ACCESS TOKEN USING DICTIONARY KEY AND STORE AS A VARIABLE
print(tokenkey) ### PRINT TOKEN KEY

track = input("Tracking? on/off: ") #### TURN TRACKING ON
while track == "on":
    url_locations = "https://ttapi.trutrakpro.co.uk/WSDataProvider.asmx/TTAssetsAllLocations" ##### ACCESS THE API TO RETREIVE LOCATION
    location_login = {
        "Token":tokenkey, ### USE TOKEN STORED
        "Filter": "your van/car ID", ### FILTER BY VAN ID
        "Record_id": "0", ### RETREIVE LAST LOCATION 
        "XMLType":"0"
        }
    
    location_response = requests.post(url_locations,data=location_login)
    location_response_xml = location_response 
    location_preview = xmltodict.parse(location_response_xml.content) ### PARSE XML FILE
    date = (location_preview["Root"]["Row"]["datetimeLocal"]) ### GET LAST DATETIME
    last_latitude = (location_preview["Root"]["Row"]["latitude"]) ### GET LAST LATITUDE 
    last_longitude = (location_preview["Root"]["Row"]["longitude"]) ### GET LAST LONGITUDE 
    last_speed = (location_preview["Root"]["Row"]["speed"]) ### GET LAST SPEED
    van = (location_preview["Root"]["Row"]["asset_identification"]) ### GET VAN REGISTRATION
    event = (location_preview["Root"]["Row"]["Event_Description"]) ### GET LAST EVENT I.E, PARKED/MOVING
    postcode = (location_preview["Root"]["Row"]["postcode"]) ### GET LAST POSTCODE
    print("---------------------------------------------------------------")
    print(f"Latitude: {last_latitude}")
    print(f"Longitude: {last_longitude}")
    print(f"Speed: {last_speed}")
    print(f"Van: {van}")                                    ############# PRINT ALL DETAILS
    print(f"Date: {date}")
    print(f"Event: {event}")
    print(f"Post Code: {postcode}")
    print("---------------------------------------------------------------")
    with open('van1.csv', 'a',newline ='') as csv_file:   #### OPEN CSV FILE
        writer = csv.writer(csv_file) ### ASSIGN CSV WRITER TO VARIABLE
        writer.writerow([str(date),str(last_latitude),str(last_longitude),str(last_speed),str(van),
                         str(event),str(postcode)]) ################ WRITE ROWS WITH THE DETAILS
        
    ################################################################################################# SAME AS ABOVE FOR THE SECOND VEHICLE 
    url_locations2 = "https://ttapi.trutrakpro.co.uk/WSDataProvider.asmx/TTAssetsAllLocations"
    location_login2 = {
        "Token":tokenkey,
        "Filter": "your van/car ID",
        "Record_id": "0",
        "XMLType":"0"
        }
    
    location_response2 = requests.post(url_locations2,data=location_login2)
    location_response_xml2 = location_response2
    location_preview2 = xmltodict.parse(location_response_xml2.content)
    date2 = (location_preview2["Root"]["Row"]["datetimeLocal"])
    last_latitude2 = (location_preview2["Root"]["Row"]["latitude"])
    last_longitude2 = (location_preview2["Root"]["Row"]["longitude"])
    last_speed2 = (location_preview2["Root"]["Row"]["speed"])
    van2 = (location_preview2["Root"]["Row"]["asset_identification"])
    event2 = (location_preview2["Root"]["Row"]["Event_Description"])
    postcode2 = (location_preview2["Root"]["Row"]["postcode"])
    print(f"Latitude: {last_latitude2}")
    print(f"Longitude: {last_longitude2}")
    print(f"Speed: {last_speed2}")
    print(f"Van: {van2}")
    print(f"Date: {date2}")
    print(f"Event: {event2}")
    print(f"Post Code: {postcode2}")
    print("---------------------------------------------------------------")
    with open('van2.csv', 'a',newline ='') as csv_file2:  
        writer2 = csv.writer(csv_file2)
        writer2.writerow([str(date2),str(last_latitude2),str(last_longitude2),str(last_speed2),str(van2),
                         str(event2),str(postcode2)])
   ##################################################################################################
    time.sleep(30) ##### SLEEP FOR 30 SECONDS THEN PULL THE DATA AGAIN
    os.system('cls') ###### CLEAR THE TERMINAL OUTPUT

    ############## NEED TO SET A BREAK IN HERE TO STOP THE APPLICATION, CURRENTLY HAVE TO KILL THE TERMINAL
    
                 


