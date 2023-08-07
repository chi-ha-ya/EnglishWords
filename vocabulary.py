import os
import csv
import random
from colorama import Fore, Style
import re
import pickle
import pandas as pd
import numpy as np
from enum import Enum

check_times = 3
freq_threshold = 100
max_list_count = 5
affix_check_times = 3


path_collins = "data/Collins_Learner's.txt"
path_en_ch = 'data/EnWords.csv'
path_words = 'data/Words.csv'
path_affixes = 'data/Affixes.csv'


class state(Enum):
    Affix = 0
    EN_CH = 1
    Collins = 2
    Else = 3


def read_words():
    words = pd.read_csv(path_words, encoding='utf-8-sig')
    return words


def read_affixes():
    affixes = pd.read_csv(path_affixes, encoding='utf-8-sig', index_col=0)
    return affixes


def read_en_ch():
    en_ch = pd.read_csv(path_en_ch, encoding='utf-8-sig')
    return en_ch


def is_prefix(str):
    return not str.startswith('~') and str.endswith('~')


def is_root(str):
    return str.startswith('~') and str.endswith('~')


def is_suffix(str):
    return str.startswith('~') and not str.endswith('~')


def sort_affix(affixes):
    # 规范格式
    affixes['affix'] = affixes['affix'].astype(str)
    affixes['affix'] = affixes['affix'].str.replace('--', '~')
    affixes['affix'] = affixes['affix'].str.replace('-', '~')

    # 去除重复
    affixes = affixes.drop_duplicates()
    affixes = affixes.dropna(subset=['affix'])

    # affix相同则合并means,以';'分隔
    affixes = affixes.groupby('affix').agg(
        {'mean': ';'.join, 'freq': 'first', 'check': 'first', 'instance': 'first'}).reset_index()

    # 选出前缀,词根,后缀,按字母顺序排序
    prefix = affixes[affixes['affix'].str.endswith('~')
                     & ~affixes['affix'].str.startswith('~')].sort_values(by='affix', ascending=True, ignore_index=True)
    root = affixes[affixes['affix'].str.startswith('~')
                   & affixes['affix'].str.endswith('~')].sort_values(by='affix', ascending=True, ignore_index=True)
    suffix = affixes[affixes['affix'].str.startswith('~')
                     & ~affixes['affix'].str.endswith('~')].sort_values(by='affix', ascending=True, ignore_index=True)
    # 重新组合
    new_affixes = pd.concat([prefix, root, suffix]).reset_index(drop=True)

    return new_affixes


def calculate_freq(affixes, words):
    # 计算词根词缀的使用次数
    affixes['freq'] = 0
    for i, row in affixes.iterrows():
        affix = str(row['affix'])
        if is_prefix(affix):
            df = words[words['word'].str.startswith(affix[:-1])]
        elif is_suffix(affix):
            df = words[words['word'].str.endswith(affix[1:])]
        elif is_root(affix):
            df = words[words['word'].str.contains(affix[1:-1])]
        affixes.at[i, 'freq'] = len(df)
    return affixes


def arrange_affixes():
    words = pd.read_csv(path_words, encoding='utf-8-sig')
    affixes = pd.read_csv(path_affixes, encoding='utf-8-sig', index_col=0)

    sorted_affixes = sort_affix(affixes)
    res = calculate_freq(sorted_affixes, words)
    res.to_csv(path_affixes, index=True, encoding='utf-8-sig')


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


def Exam():
    # 随机抽一个单词,给出正确和错误(随机)释义二选一,选对3次则考察一次拼写,拼写也正确则加入熟记名单退出考察
    df = pd.read_csv(path_list, encoding='utf-8-sig')
    df['checked'] = check_times
    # print(df)
    while True:
        e = df.sample().iloc[0]
        answer = e['word'].lower()
        print(e['mean'])
        guess = guess('▶: ')
        if guess == '':
            print(e['word']+' : ', e['mean']+'\n')
        elif guess == answer:
            print(Fore.GREEN + 'right!' + '\n' + Style.RESET_ALL)
            df.at[e.name, 'checked'] -= 1
            if df.at[e.name, 'checked'] <= 0:
                df = df[df['word'] != e['word']]
        elif guess == '---':
            df.to_csv('test.csv', encoding='utf-8-sig', index=False)
        else:
            print(Fore.RED + 'wrong!    ' + Style.RESET_ALL +
                  e['word']+' : ', e['mean']+'\n')


def search_in_collins(word, collins, fuzzy=False):
    words = []
    for k, v in collins.items():
        if fuzzy:
            if word in k:
                words.append(v)
        else:
            if word == k:
                return v
    return words


def search_in_en_ch(word, en_ch, fuzzy=True):
    if fuzzy:
        words = en_ch[en_ch['word'].str.contains(word)]
    else:
        words = en_ch[en_ch['word'] == word]
    return words


def search_in_words(word, words, fuzzy=True):

    if fuzzy:
        words = words[words['word'].str.contains(word)]
    else:
        words = words[words['word'] == word]
    return words


def print_all_command():

    print('--help | --h'.ljust(10)+':'+'帮助')
    print('--arrange | --arr'.ljust(10)+':'+'整理词根词缀文档')


def parse_command(input):
    if input == '--help' or input == '--h':
        print_all_command()

    elif input == '--arrange' or input == '--arr':
        print('整理词根词缀文档...')
        arrange_affixes()
        print(Fore.GREEN+'整理完毕'+Style.RESET_ALL)
    else:
        print(Fore.RED+'not legal command'+Style.RESET_ALL)


if __name__ == "__main__":
    words = read_words()
    affixes = read_affixes()
    en_ch = read_en_ch()
    collins = create_collins_dict()

    # affixes = affixes[affixes['freq'] > freq_threshold]
    affixes = affixes[affixes['check'] >= affix_check_times]

    flg = True
    while True:
        print(Fore.CYAN+'---------------------------------------------------------------------'+Style.RESET_ALL)

        if flg:
            affix = affixes.sample(n=1).iloc[0]
            x = affix['affix']
            answer = affix['affix'].replace('~', '')
            if is_prefix(x):
                list_word = words[words['word'].str.startswith(x[:-1])]
            elif is_suffix(x):
                list_word = words[words['word'].str.endswith(x[1:])]
            elif is_root(x):
                list_word = words[words['word'].str.contains(x[1:-1])]

            if len(list_word) > max_list_count:
                list_word = list_word.sample(max_list_count)
            for i, row in list_word.iterrows():
                print(row['word'].ljust(25) + ' : ', row['mean'])

        guess = input('▶: ')
        if guess == answer:
            print(Fore.GREEN + 'right!    ' +
                  Fore.CYAN + affix['affix'].rjust(15) +
                  Fore.WHITE + ' : ' +
                  Fore.CYAN + affix['mean'] + '\n' + Style.RESET_ALL)
            flg = True
        elif guess.startswith('--'):
            parse_command(guess)
            flg = False
        elif is_prefix(guess):
            print(Fore.CYAN+'---------------------------------------------------------------------'+Style.RESET_ALL)
            res = words[words['word'].str.startswith(guess[:-1])]
            if len(res) > max_list_count:
                res = res.sample(max_list_count)
            for index, row in res.iterrows():
                print(row['word'].ljust(25) + ' : ', row['mean'])
            flg = False
        elif is_suffix(guess):
            print(Fore.CYAN+'---------------------------------------------------------------------'+Style.RESET_ALL)
            res = words[words['word'].str.endswith(guess[1:])]
            if len(res) > max_list_count:
                res = res.sample(max_list_count)
            for index, row in res.iterrows():
                print(row['word'].ljust(25) + ' : ', row['mean'])
            flg = False
        elif is_root(guess):
            print(Fore.CYAN+'---------------------------------------------------------------------'+Style.RESET_ALL)
            res = words[words['word'].str.contains(guess[1:-1])]
            if len(res) > max_list_count:
                res = res.sample(max_list_count)
            for index, row in res.iterrows():
                print(row['word'].ljust(25) + ' : ', row['mean'])
            flg = False
        elif ':' in guess:
            res = search_in_collins(guess.replace(':', ''),  collins)
            print(Fore.CYAN+'---------------------------------------------------------------------'+Style.RESET_ALL)
            print(res)
            flg = False
        elif guess == '':
            flg = True
        else:
            print(Fore.RED + 'wrong!    ' +
                  Fore.CYAN + affix['affix'].rjust(15) +
                  Fore.WHITE + ' : ' +
                  Fore.CYAN + affix['mean'] + '\n' + Style.RESET_ALL)
            flg = True
