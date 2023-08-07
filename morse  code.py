# -*- coding: utf-8 -*-
import random
from colorama import Fore, Style

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

morseCode = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
             '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
             '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',]

if __name__ == "__main__":
    while True:
        n = random.randint(0, 25)
        select = random.randint(0, 1)
        # select = 1
        quest = alphabet[n] if select == 0 else morseCode[n]
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + quest + Style.RESET_ALL)

        if select == 0:
            guess = input("Input Morse Code:")
            if guess == morseCode[n]:
                print(Fore.GREEN + "right!")
            else:
                print(Fore.RED + "wrong!    " +
                      Fore.CYAN + f"{quest}" +
                      Fore.WHITE + " Morse Code is: " +
                      Fore.CYAN + morseCode[n]
                      )
        else:
            guess = input("Input Alphabet:")
            if guess == alphabet[n]:
                print(Fore.GREEN + "right!")
            else:
                print(Fore.RED + "wrong!    " +
                      Fore.CYAN + f"{quest}" +
                      Fore.WHITE + " Alphabet is: " +
                      Fore.CYAN + alphabet[n]
                      )

        print('\n' + Style.RESET_ALL)
