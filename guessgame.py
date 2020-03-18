print("Let's Play a guessing game")
print("You only get 3 attempts")
secret = 7
count = 0
count_limit = 3
while count < count_limit:
    guess = int(input("Guess: "))
    count = count + 1
    if guess == secret:
        print("You win!")
        break
else:
    print("Sorry, You Lose")
