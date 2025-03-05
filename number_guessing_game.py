import random

rnum = random.randint(1, 100)
while True:
    try:
        number = int(input("Guess the number between 1 and 100: "))

        if number > rnum:
            print("Too high!")
        elif number < rnum:
            print("Too low!")
        else:
            print("Congratulations! You guessed the number.")
            break
            
    except ValueError:
        print("Please enter a valid number")