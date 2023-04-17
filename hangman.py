import random

# Write your code here
print("H A N G M A N")
print()

words_list = ["python", "java", "swift", "javascript"]

attempts = 8
run = True
play = False
won = 0
lost = 0

while run:
    user_input = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")

    if user_input == 'exit':
        break
    elif user_input == 'play':
        random_word = random.choice(words_list)
        letters_set = set(random_word)
        user_letter_set = set()
        hyphen_str = ["-" for _ in random_word]
        attempts = 8

        play = True
    elif user_input == 'results':
        print(f"You won: {won} times")
        print(f"You lost: {lost} times")

    while play:
        print(''.join(hyphen_str))
        if ''.join(hyphen_str) == random_word:
            print(f"You guessed the word {random_word}!")
            print("You survived!")
            won += 1
            play = False
            break

        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("Please, input a single letter.")
            print()
            continue
        if letter == letter.title():
            print("Please, enter a lowercase letter from the English alphabet.")
            print()
            continue

        if letter in hyphen_str or letter in user_letter_set:
            print("You've already guessed this letter.")
        elif letter in letters_set:
            if random_word.count(letter) > 1:
                indices = [i for i, x in enumerate(random_word) if x == letter]
                for indice in indices:
                    hyphen_str[indice] = letter
            elif letter in letters_set:
                letter_index = random_word.index(letter)
                hyphen_str[letter_index] = letter
        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1
        user_letter_set.add(letter)
        print()
        if attempts == 0:
            print("You lost!")
            lost += 1
            play = False
            break
