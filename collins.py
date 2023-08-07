import os
import csv
import random
from colorama import Fore, Style
import re
import pickle
import pandas as pd
import numpy as np
from enum import Enum

path_collins = "data/Collins_Learner's.txt"
# path_en_ch = 'data/EnWords.csv'
# path_words = 'data/Words.csv'
# path_affixes = 'data/Affixes.csv'


def extract_words(content):
    pattern = r'★☆☆\s+(.+?)[○●]*\n'
    word = re.findall(pattern, content)[0]
    explain = re.sub(pattern, '', content)
    return word.strip(), explain.strip()


def create_collins_dict(txt_file_path=path_collins):
    word_dict = {}
    with open(txt_file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
        matches = content.split('——————————————')
        for match in matches:
            if match != '':
                word, explain = extract_words(match)
                word_dict[word] = explain

    return word_dict


if __name__ == "__main__":
    collins = create_collins_dict()

    while True:
        guess = input('▶: ')
        try:
            explain = collins[guess]
            if explain == '':
                print('not find ' + guess)
            else:
                print(explain)
        except:
            print('not find ' + guess)

        print(Fore.CYAN+'---------------------------------------------------------------------'+Style.RESET_ALL)
