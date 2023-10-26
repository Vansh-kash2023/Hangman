from collections import deque
import random

r = True

while r:
    print("Welcome to the Hangman Game")
    print("You have to guess the letters of a fruit's name. All the best. Let's begin...")

    fruits = deque(["Mango", "Orange", "Watermelon", "Papaya", "Pomegranate", "Strawberry"])
    selected_fruit = random.choice(fruits)
    num_letters = len(selected_fruit)

    print("You have to enter", num_letters, "letters")
    print("You will get", num_letters + 3, "chances to type the correct word")

    guessed_word = ""
    attempts = 0

    for i in range(num_letters):
        while attempts < num_letters + 3:
            attempts += 1
            guess = input("Enter the " + str(i + 1) + " letter of the Fruit: ")
            if guess.lower() == selected_fruit[i].lower():
                print("Correct!")
                attempts -= 1
                guessed_word += guess
                break
            else:
                print("Incorrect input. Try again!")

    if guessed_word.lower() == selected_fruit.lower():
        print("Congratulations! You won the game.")
    else:
        print("You lose. The correct word was '" + selected_fruit + "'.")

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() != 'y':
        print("Game ended")
        r = False
    