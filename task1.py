#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
x = 59
print("I'm thinking of a number between 1 & 100 \nYou have 10 guesses")
for i in range(10):
    y = input(f"Guess #{i+1}: ")
    y = int(y)
    if y > 100 or y < 1:
     print("The number is between 1 & 100")
     continue
    if y == x:
        print(f"Thats correct, the number = {x}")
        break
    if y > x:
        print("Thats too high")
        if i == 9:
         print("Game over")
    if y < x:
        print("Thats too low")
        if i == 9:
         print("Game over")
   


