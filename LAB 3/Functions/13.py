import random

a = str(input("Hello! What's your name?\n"))
print(f"Well, {a}, I'am thinking of a number between 1 and 20")
x = random.randint(1, 20)
count = 0
print(x)

while count < 20:
    count += 1
    guess = int(input("Take a guess.\n"))
    if x == guess:
        print(f"Good job, {a}! You guessed my number in {count} guesses!")
        break
    elif x > guess:
        print("Your guess is too low.")
    elif x < guess:
        print("Your guess is too high")

