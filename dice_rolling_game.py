import random

while True:
    q = input("Roll the dice? (y/n): ").lower()
    if q == 'n':
        print("Thanks for playing!")
        break
    elif q == 'y':
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(f'({d1}, {d2})')
    else:
        print("Invalid choice!")