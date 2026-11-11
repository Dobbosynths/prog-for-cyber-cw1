import security_tools                           #Import the python file security_tools

password = ""                                   #Initialise variables
ip = ""

ip = str(input("Enter an IP: "))                #Ask the user for an IP
password = str(input("Enter your password: "))  #Ask the user for a password

if security_tools.validate_ip(ip):              #Use the function validate_ip from the python file security_tools. This will check to see if the IP is valid. If the function returns True print:
    print("Your IP is valid")
else:                                           #If the function returns False print:
    print("Your IP is invalid") 


if security_tools.pass_checker(password):       #Use the function pass_checker from the python file security_tools. This will check to see if the password is strong or not. If the function returns True print:
    print("Your password is strong")            
else:                                           #If the function returns False print:
    print("Your password is weak")
    security_tools.pass_generator()             #Then call the function pass_generator from the python file security_tools. This will randomly generate a strong passsword and suggest it to the user
    
