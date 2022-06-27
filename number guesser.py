import random

print("Random numbers generated from 1-10 , can you guess it?")

def random_number(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input("Enter your guess: "))
        if guess > random_number:
            print("Your guess was too high")
        elif guess < random_number:
            print("You guess was too low")
    print(f"Congrats, you guess the {random_number} number.")

random_number(10)
