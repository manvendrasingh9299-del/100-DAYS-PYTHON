import random

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nGuess a number (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too low! Try a bigger number.")

    elif guess > secret_number:
        print("📈 Too high! Try a smaller number.")

    else:
        print("\n🎉 Congratulations! You won!")
        print("Secret Number:", secret_number)
        print("Total Attempts:", attempts)
        break

print("\nThanks for playing!")