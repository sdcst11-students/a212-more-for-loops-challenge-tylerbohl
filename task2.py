#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == expectedUsername and password == expectedPassword:
        print("Access granted")
        break
    elif i == 2:
        print("System locked")
    else:
        print(f"Wrong Username or Passwoed\nYou have {2-i} attempts left")

