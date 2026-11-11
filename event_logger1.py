import random
import socket
from datetime import datetime

username = []                   #Initialise all variables
password = ""
trueusername = "admin"          #The correct username
truepassword = "manhunt43"      #The correct password
position = 0
guesses = 0
event = []
event_id = []
timestamp = []
ip_address = []

username.append(input("Username: "))    #Ask the user for their username
password=input("Password: ")            #Ask the user for their password
guesses += 1                            #Count number of guesses
event_id.append(random.randint(1000,9999))  #Assign the event id
timestamp.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  #Get the timestamp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address.append(s.getsockname()[0])   #Get the ip address
print("")

while (username[position] != trueusername) or (password != truepassword):   #While the users credentials dont match keep asking for credentials
    position += 1
    guesses += 1
    username.append(input("Username: "))
    password=input("Password: ")
    event_id.append(random.randint(1000,9999))
    event.append("Failed Login")    #Because the users credentials dont match mark this event as a "Failed Login"
    timestamp.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address.append(s.getsockname()[0])
    print("")

if (username[position] == trueusername) and (password == truepassword):
    event.append("Successfull Login")   #Because the users credentials do match mark this event as a "Successful Login"

for loop in range(guesses):     #Run a loop for the amount of times the user entered his credentials
    print("SECURITY EVENT LOG")     #Print the log of each login attempt
    print("===================")
    print("Event ID: ",event_id[loop])
    print("Username: ",username[loop])
    print("IP Address: ",ip_address[loop])
    print("Event: ",event[loop])
    print("Timestamp: ",timestamp[loop])
    print("")
