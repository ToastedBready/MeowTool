import requests
import time
import random
import sys
from colorama import Fore

def Playfab_Spam():
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
 webhook2 = input(str("Enter Webhook URL: "))
 requests.delete(webhook2)

def Webhook_Info():
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

print(Fore.BLUE + "████████╗ ██████╗  █████╗ ███████╗████████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗")
print("╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝")
print("   ██║   ██║   ██║███████║███████╗   ██║   ███████╗       ██║   ██║   ██║██║   ██║██║     ███████╗")
print("   ██║   ██║   ██║██╔══██║╚════██║   ██║   ╚════██║       ██║   ██║   ██║██║   ██║██║     ╚════██║")
print("   ██║   ╚██████╔╝██║  ██║███████║   ██║   ███████║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║")
print("   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝")
print("------------------------------------------------------------------" + Fore.RESET)
print(Fore.LIGHTBLUE_EX + "")
print("Webhook Spammer [1]       Webhook Deleter [2]")
print("Playfab Spammer [3]       Webhook Info    [4]")
print("")
print("[Quit]")
print("")
Option = input("Option: ")
if Option == "1":
 Webhook_Spam()
elif Option == "2":
 Webhook_Delete()
elif Option == "3":
 Playfab_Spam()
elif Option == "4":
 Webhook_Info()
elif Option == "quit":
 print("See ya!")
