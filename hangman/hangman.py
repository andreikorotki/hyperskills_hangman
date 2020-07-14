import random
import json

words = ['python', 'java', 'kotlin', 'javascript']
attempts = 8


def game(attempts, words):
    letter_list = []

    def letter_cache(letter):
        if letter not in letter_list:
            letter_list.append(letter)
            return False
        else:
            return True

    i = random.randint(0, len(words) - 1)
    tmp_word = words[i][0:0].ljust(len(words[i]), "-")
    print("")
    while attempts > 0:
        print(tmp_word)
        matcher = 0
        print(json.dumps("Input a letter:"))
        guessed_letter = input()
        tmp = ''
        for k, v in enumerate(words[i]):
            if guessed_letter == v:
                tmp += v
                matcher += 1
            else:
                tmp += tmp_word[k]
        if 1 < len(guessed_letter) or len(guessed_letter) <= 0:
            print("You should input a single letter")
        elif (not guessed_letter.islower()) or (not guessed_letter.isascii()):
            print("It is not an ASCII lowercase letter")
        elif letter_cache(guessed_letter):
            # and guessed_letter in words[i]:
            print("You already typed this letter")
        elif matcher > 0:
            tmp_word = tmp
        else:
            print("No such letter in the word")
            attempts -= 1
        if tmp_word == words[i]:
            print("You guessed the word!")
            print("You survived!")
            break
        elif attempts == 0:
            print("You are hanged!")
        print("")


def main_menu():
    game_name = 'H A N G M A N'
    greeter = 'Type "play" to play the game, "exit" to quit:'
    print(game_name)

    while True:
        print(greeter)
        user_input = input()
        if user_input == "play":
            game(attempts, words)
        elif user_input == "exit":
            break
        else:
            continue


main_menu()
