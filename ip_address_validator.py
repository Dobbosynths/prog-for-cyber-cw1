ip = ""                             #Initialise ip variable

ip = str(input("Enter an IP address: "))    #Ask the user to enter an ip address

def validate_ip(ip):                        #Define the function validate_ip with the string ip as a parameter. This function will be used to check if the ip is valid or not
    ip = ip.strip()                         #Strip all leading and trailing whitespace
    if "." not in ip:                       #Check to see if the ip address contains dots
        return False
    if ip.count(".") != 3:                  #Check if there are exactly three dots
        return False
    parts = ip.split(".")                   #Split the ip into four parts
    if len(parts) != 4:                     #Check that there are four parts
        return False
    for loop in range(0,4):                 #Run a loop 4 times for each part
        if not parts[loop].isdigit():       #Check that each part contains only digits
            return False
        number = int(parts[loop])           #Convert each part into an integer
        if number < 0 or number > 255:      #Check that the number is between 0 and 255
            return False
    return True                             #If the ip passes all these checks return True

if validate_ip(ip):                         #If the function returns true then print:
    print("Valid IP Address")
else:                                       #If the function returns false then print:
    print("Invalid IP Address")
