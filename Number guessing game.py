import random

difficulty=input("Select difficulty level (easy, medium, hard): ")
if difficulty == "easy":
    num=random.randint(1,25)
    trys=10
elif difficulty == "medium":
    num=random.randint(1,50)
    trys=7
else:
    num=random.randint(1,100)
    trys=5

print("Welcome to the number guessing game")
name=input("Enter your name= ")
print("HI " + name + ", I have selected a number between 1 and 100, you have " + str(trys) + " tries to guess it")
guess=int(input("Enter your guess= "))

while guess != num and trys > 0:
    if(guess < num):
        print("Try a higher number")
        guess=int(input("Enter your guess= "))
        trys -= 1
    elif(guess > num):
        print("Try a smaller number")
        guess=int(input("Enter your guess= "))
        trys -= 1
else:
    if(guess == num):
        print("You won " + name + "🎉")
    else:
        print("You lost " + name + " the number was ",num)


