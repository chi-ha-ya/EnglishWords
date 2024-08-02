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
path_en_ch = 'data/EnWords.csv'
path_words = 'data/Gee.csv'
path_affixes = 'data/Affixes.csv'


def read_words():
    words = pd.read_csv(path_words, encoding='utf-8-sig')
    return words


def read_affixes():
    affixes = pd.read_csv(path_affixes, encoding='utf-8-sig', index_col=0)
    return affixes


def extract_words(content):
    pattern = r'★☆☆\s+(.+?)[○●]*\n'
    word = re.findall(pattern, content)[0]
    explain = re.sub(pattern, '', content)
    return word.strip(), explain.strip()


def read_en_ch():
    en_ch = pd.read_csv(path_en_ch, encoding='utf-8-sig')
    return en_ch


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


def is_prefix(str):
    return not str.startswith('~') and str.endswith('~')


def is_root(str):
    return str.startswith('~') and str.endswith('~')


def is_suffix(str):
    return str.startswith('~') and not str.endswith('~')


def mask_word(word):
    l = len(word)
    n = random.randint(1, 4)
    letters = list(word)
    indices = random.sample(range(l), n)
    indices = sorted(indices)
    for i in indices:
        letters[i] = '_'
    new_word = ''.join(letters)
    replaced_letters = ''.join([word[i] for i in indices])
    return new_word, replaced_letters


if __name__ == "__main__":
    words = read_words()
    affixes = read_affixes()
    en_ch = read_en_ch()
    collins = create_collins_dict()

    words_to_check = words[words['check'].isna()]
    if words_to_check.empty:
        input(Fore.GREEN+'all words have been checked!'+Style.RESET_ALL)

    while True:
        df = words_to_check.sample(n=1).iloc[0]
        print(df['mean'])

        new_word, replaced_letters = mask_word(df['word'])

        print(new_word)

        guess = input('▶: ')
        if guess.startswith(' '):
            qurry = guess.replace(' ', '')
            print(Fore.CYAN+'---------------------------------------------------------------------'+Style.RESET_ALL)
            explain = collins[qurry]
            if explain == '':
                print('not find ' + Fore.CYAN + qurry + Style.RESET_ALL)
            else:
                print(explain)
            print(Fore.CYAN+'---------------------------------------------------------------------'+Style.RESET_ALL)

        elif guess == 'save':
            x = words[~words['word'].isin(words_to_check['word'])]
            words.loc[x.index, 'check'] = '☆'
            words.sort_values(by='word', inplace=True)
            words.dropna(subset=['word'], inplace=True)
            words.to_csv(path_words, encoding='utf-8-sig', index=False)
            print(Fore.CYAN + 'saved!'+Style.RESET_ALL)

        elif is_prefix(guess):
            list_word = words_to_check[words_to_check['word'].str.startswith(
                guess[:-1])]
            print(list_word)
        elif is_suffix(guess):
            list_word = words_to_check[words_to_check['word'].str.endswith(
                guess[1:])]
            print(list_word)
        elif is_root(guess):
            list_word = words_to_check[words_to_check['word'].str.contains(
                guess[1:-1])]
            print(list_word)
        elif guess == replaced_letters:
            print(Fore.GREEN + 'right! ' +
                  Style.RESET_ALL + df['word'] + ' : ', df['mean']+'\n')
            words_to_check = words_to_check[words_to_check['word']
                                            != df['word']]
        else:
            print(Fore.RED + df['word'] +
                  Style.RESET_ALL + ' : ', df['mean']+'\n')
