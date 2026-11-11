import os, random, string

def pass_checker(password):                 #Define the function pass_checker with the password string as a parameter. This function will be used to check passwords
    password = password.strip()             #Strip password of all white space
    if len(password) < 8:                   #If the password does not have a length of longer than 8 characters then return false
        return False
    has_letter = False                      #Initialise variables
    has_digit = False
    has_symbol = False
    for c in password:                      #For every character in password:
        if c.isalpha():                     #Check to see if the character is a letter
            has_letter = True               #If the character is a letter make has_letter = true
        elif c.isdigit():                   #Check to see if the character is a number
            has_digit = True                #If the character is a number make has_number = true
        else:                               #Else means the character must be a symbol
            has_symbol = True               #If the character is a symbol make has_symbol = true
    if has_letter == True and has_digit == True and has_symbol == True:     #If the password has a letter,number and symbol then return true
        return True
    else:                                                                   #If it does not return false
        return False

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

def pass_generator():                               #Define the function pass_generator. This function will be used to generate strong passwords
    rand_password = []                              #Initialise variable
    length = random.randint(10, 16)                 #Length is randomised between 10-16
    chars = string.ascii_letters + string.digits + string.punctuation   #Characters used are a mix between letters,numbers and symbols
    for i in range(length):                         #Run a loop for however long the length of the password will be
        randomchar = random.choice(chars)           #For each loop cycle choose a random character
        rand_password.append(randomchar)            #Append this random charcter to the list rand_password
    print("You can use this randomised password instead: " + "".join(rand_password))     #Once the loop has ran. Join all the charcters together and suggest the randomised strong password
