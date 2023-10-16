#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""
users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]
print(users[0])

for i in users:
    username = input("Enter username: ")
    password = input("Enter password: ")
    username = str(username)
    password = str(password)
    for o in users:
     if username == users[o] and password == passwords[o]:
      print("Access granted")
      break
    else:
        print("Invalid login")

