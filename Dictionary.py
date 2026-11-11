dictionary = {"username": "Peter", "ip": "192.168.0.1", "event_type": "Bad", "risk_level": 5}

print("The username in the dictionary is ",dictionary["username"])   #Display the username in the dictionary
print("The IP Address in the dictionary is",dictionary["ip"])         #Display the ip address in the dictionary

dictionary["status"] = "Up"     #Added a new field to the dictionary called 'status'
dictionary["risk_level"] = 8    #Updated the risk level to 8
del dictionary["event_type"]    #Removed the event_type field from the dictionary

print("\nThe updated dictionary ",dictionary)               #Print the dictionary

count = len(dictionary)         #Count the number of key-value pairs in the dictionary
print("\nThe number of key value pairs: ",count)                    #Display the number of key-value pairs
