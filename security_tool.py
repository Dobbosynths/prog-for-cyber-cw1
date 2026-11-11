security_code = 4032                    #Initialise variables #The security code to access the security tool
code_guess = 0
menu = True
correct_password = "choco"              #The password for the Security Event Counter
brute_pass = "$tore43"                  #The password for the Brute-Force Simulation
account_username = "stephend"           #The username for the Login Authentication
account_pass = "yungpups##"             #The password for the Login Authentication
username = ""
password = ""
correct_guesses = 0
incorrect_guesses = 0
percentage = 0.0
attempts = 0

try:                                                                                                #Error handling. If the user does not enter a number for the security code guess
    code_guess = int(input("Please enter the security code to gain access to this program: "))      #Ask the user for the security code to access the security tool
    if code_guess == security_code:                                                                 #Start the menu if the user gets the security code right(4032)
        while menu == True:                                                                         #Run the menu continuously unless the user chooses to quit
            print("\nSECURITY TOOL")
            print("=============")
            print("1)Security Event Counter")
            print("2)Brute-Force Simulation")
            print("3)Login Authentication")
            print("4)Exit")
            try:                                                                                        #Error handling. If the user does not enter a number for the menu
                userchoice=int(input("Enter a number to select an option: "))                           #Asks the user to choose an option from the menu
                if userchoice == 1:                                                                     #If the user chooses 1 then:
                    for loop in range(0,10):                                                            #Run a loop 10 times
                        password = str(input("Please enter a password: "))                              #Ask the user to enter a password
                        if password == correct_password:                                                #If the user entered password matches the correct password 'choco'
                            correct_guesses +=1                                                         #Add 1 to correct guesses
                        else:
                            incorrect_guesses +=1                                                       #If not then add 1 to incorrect guesses
                    percentage = ((incorrect_guesses / 10) * 100)                                       #Calculate the percentage of incorrect guesses
                    if percentage > 50:                                                                 #If the percentage of incorrect guesses is above 50% then print an alert
                        print("\nALERT! The number of incorrect passwords was above %50")
                        print("The percentage of incorrect passwords was %",percentage)                 #Display percentage of incorrect guesses
                    else:
                        print("\nThe percentage of incorrect passwords was %",percentage)
                    correct_guesses = 0                                                                 #Reset the count of correct and incorrect guesses
                    incorrect_guesses = 0
                elif userchoice == 2:                                                                   #If the user chooses 2 then:
                    password = ""                                                                       #Reset password variable and attempts variable
                    attempts = 0
                    while password != brute_pass:                                                       #While the user entered password does not match the brute force password $tore43 then:
                        password = str(input("What is your password guess?: "))                         #Ask the user for their password guess
                        attempts +=1                                                                    #Count number of attempts to guess the password
                        if password == brute_pass:                                                      #If the user guesses the password right then print:
                            print("\nWell Done! You guessed the password")
                        elif attempts >= 3:                                                             #If the user does not manage to guess the password in 3 attempts then break the while loop and print:
                            print("\nSorry you have reached the maximum number of attempts allowed")
                            break
                elif userchoice == 3:                                                                   #If the user chooses 3 then:
                    password = ""                                                                       #Reset the password,username and attempts variables
                    username = ""
                    attempts = 0
                    while password != account_pass or username != account_username:                     #While the user entered username or password doesnt match the correct username and password then:
                        username = str(input("\nUsername: "))                                           #Ask the user for their username
                        password = str(input("Password: "))                                             #Ask the user for their password
                        attempts +=1                                                                    #Count number of attempts to enter the correct username and password
                        if password == account_pass and username == account_username:                   #If the user enters the correct username and password then break the while loop and print:
                            print("\nAuthentication Succeeded")
                            break
                        elif password != account_pass or username != account_username:                  #If the user enters the wrong username or password then print:
                            print("\nAuthentication Failed")
                        if attempts >= 3:                                                               #If the user reaches 3 failed attempts then break the while loop and freeze the account for 24 hours
                            print("\nSorry you have reached the maximum number of attempts allowed")
                            print("Your account will now be frozen for 24 hours")
                            break
                elif userchoice == 4:                                                                   #If the user chooses 4 then:
                    print("\nThank you for using the security tool")                                    #Print a goodbye message
                    menu = False                                                                        #Quit the menu
            except ValueError:                                                                          #If the user does not enter a number for the menu then print:
                print("\nInvalid Input. You did not enter a number!")
        else:                                                                                                   #If the user gets the security code wrong then print:
            print("\nThe security code you entered was wrong you will not be allowed access to this program")
except ValueError:                                          #If the user does not enter a number for the security code guess then print:
    print("\nInvalid Input. You did not enter a number!")
