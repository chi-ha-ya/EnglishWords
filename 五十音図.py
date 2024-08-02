# -*- coding: utf-8 -*-
import csv
import random
from colorama import Fore, Style

hiragana = ['あ', 'い', 'う', 'え', 'お',
            'か', 'き', 'く', 'け', 'こ', 'きゃ', 'きゅ', 'きょ',
            'さ', 'し', 'す', 'せ', 'そ', 'しゃ', 'しゅ', 'しょ',
            'た', 'ち', 'つ', 'て', 'と', 'ちゃ', 'ちゅ', 'ちょ',
            'な', 'に', 'ぬ', 'ね', 'の', 'にゃ', 'にゅ', 'にょ',
            'は', 'ひ', 'ふ', 'へ', 'ほ', 'ひゃ', 'ひゅ', 'ひょ',
            'ま', 'み', 'む', 'め', 'も', 'みゃ', 'みゅ', 'みょ',
            'や', 'ゆ', 'よ',
            'ら', 'り', 'る', 'れ', 'ろ', 'りゃ', 'りゅ', 'りょ',
            'わ', 'を', 'ん',
            'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ぎゃ', 'ぎゅ', 'ぎょ',
            'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'じゃ', 'じゅ', 'じょ',
            'だ', 'ぢ', 'づ', 'で', 'ど',
            'ば', 'び', 'ぶ', 'べ', 'ぼ', 'びゃ', 'びゅ', 'びょ',
            'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'ぴゃ', 'ぴゅ', 'ぴょ'
            ]

katakana = ['ア', 'イ', 'ウ', 'エ', 'オ',
            'カ', 'キ', 'ク', 'ケ', 'コ', 'キャ', 'キュ', 'キョ',
            'サ', 'シ', 'ス', 'セ', 'ソ', 'シャ', 'シュ', 'ショ',
            'タ', 'チ', 'ツ', 'テ', 'ト', 'チャ', 'チュ', 'チョ',
            'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ニャ', 'ニュ', 'ニョ',
            'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'ヒャ', 'ヒュ', 'ヒョ',
            'マ', 'ミ', 'ム', 'メ', 'モ', 'ミャ', 'ミュ', 'ミョ',
            'ヤ', 'ユ', 'ヨ',
            'ラ', 'リ', 'ル', 'レ', 'ロ', 'リャ', 'リュ', 'リョ',
            'ワ', 'ヲ', 'ン',
            'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ギャ', 'ギュ', 'ギョ',
            'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ジャ', 'ジュ', 'ジョ',
            'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
            'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'ビャ', 'ビュ', 'ビョ',
            'パ', 'ピ', 'プ', 'ペ', 'ポ', 'ピャ', 'ピュ', 'ピョ',

            'ツァ', 'ファ', 'ウィ', 'ティ', 'フィ', 'ディ', 'トゥ',
            'ドゥ', 'ヂュ', 'ウェ', 'シェ', 'チェ', 'ツェ', 'フェ',
            'ジェ', 'ウォ', 'ツォ', 'フォ'
            ]

nomaji = ['a', 'i', 'u', 'e', 'o',
          'ka', 'ki', 'ku', 'ke', 'ko', 'kya', 'kyu', 'kyo',
          'sa', 'shi', 'su', 'se', 'so', 'sha', 'shu', 'sho',
          'ta', 'chi', 'tsu', 'te', 'to', 'cha', 'chu', 'cho',
          'na', 'ni', 'nu', 'ne', 'no', 'nya', 'nyu', 'nyo',
          'ha', 'hi', 'fu', 'he', 'ho', 'hya', 'hyu', 'hyo',
          'ma', 'mi', 'mu', 'me', 'mo', 'mya', 'myu', 'myo',
          'ya', 'yu', 'yo',
          'ra', 'ri', 'ru', 're', 'ro', 'rya', 'ryu', 'ryo',
          'wa', 'wo', 'n',
          'ga', 'gi', 'gu', 'ge', 'go', 'gya', 'gyu', 'gyo',
          'za', 'ji', 'zu', 'ze', 'zo', 'ja', 'ju', 'jo',
          'da', 'ji', 'zu', 'de', 'do',
          'ba', 'bi', 'bu', 'be', 'bo', 'bya', 'byu', 'byo',
          'pa', 'pi', 'pu', 'pe', 'po', 'pya', 'pyu', 'pyo',

          'tsa', 'fa', 'wi', 'ti', 'fi', 'di', 'tu', 'du', 'dyu',
          'we', 'she', 'che', 'tse', 'fe', 'je', 'wo', 'tso', 'fo'
          ]

# checked = ['あ', 'い', 'う', 'え', 'か', 'く', 'け', 'こ', 'し', 'す',
#              'せ', 'そ', 'た', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね',
#              'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'も',
#              'や', 'ゆ', 'よ', 'り', 'る', 'れ', 'ろ', 'を', 'ん', 'ア',
#              'イ', 'エ', 'カ', 'キ', 'ケ', 'コ', 'サ', 'ス', 'セ', 'テ',
#              'ト', 'ナ', 'ニ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
#              'マ', 'モ', 'ヤ', 'ユ', 'ヨ', 'リ', 'レ', 'ン', 'ひゃ', 'ら',
#              'ロ', 'ニュ', 'キャ', 'オ', 'ミ', 'にゃ', 'リョ', 'メ', 'キョ', 'ぷ',
#              'きょ', 'ニョ', 'が', 'りゅ', 'ぞ', 'ル', 'ぜ', 'べ', 'みゅ', 'ツォ',
#              'しゅ', 'ヒュ', 'ニャ', 'ミャ', 'ど', 'グ', 'リュ', 'びゅ', 'パ', 'ベ',
#              'ヒャ', 'りゃ', 'で', 'しょ', 'ぽ', 'シュ', 'キュ', 'ぎゅ', 'ギ', 'き',
#              'お', 'ド', 'め', 'ツ', 'リャ', 'きゃ', 'ぐ', 'ゼ', 'ザ', 'にょ',
#              'ゾ', 'わ', 'ご', 'バ', 'きゅ', 'ピュ', 'ポ', 'ソ', 'ワ', 'みゃ',
#              'ビョ', 'シャ', 'タ', 'ぴ', 'ぎょ', 'ファ', 'ちゅ', 'ズ', 'ギョ', 'ミョ',
#              'びゃ', 'ミュ', 'ず', 'ギュ', 'だ', 'ひょ', 'みょ', 'ぶ', 'ム', 'ぼ',
#              'ツァ', 'ウ', 'ギャ', 'ビ', 'ラ', 'にゅ', 'ディ', 'ガ', 'ク', 'ゴ',
#              'りょ', 'ぎ', 'ば', 'ぎゃ', 'ペ', 'しゃ', 'ジャ', 'じゃ', 'ビャ', 'ブ',
#              'び', 'げ', 'ピ', 'ウェ', 'ぴゅ', 'シェ', 'ちょ', 'びょ', 'ツェ', 'ぺ',
#              'ティ', 'プ', 'じ', 'ボ', 'ジュ', 'じゅ', 'ゲ', 'ビュ', 'ヒョ', 'シ',
#              'トゥ', 'ひゅ', 'にゅ', 'ディ', 'ガ', 'ク', 'ゴ', 'りょ', 'ぎ', 'ば',
#              'ぎゃ', 'ペ', 'しゃ', 'ジャ', 'じゃ', 'ビャ', 'ブび', 'げ', 'ピ', 'ウェ',
#              'ぴゅ', 'シェ', 'ちょ', 'びょ', 'ツェ', 'ぺ', 'ティ', 'プ', 'じ', 'ボ',
#              'ジュ', 'じゅ', 'ゲ', 'ビュ', 'ヒョ', 'ひゅ', 'ぱ', 'ダ', 'にょ',
#              'ヒャ', 'ティ', 'ミョ', 'チョ', 'ぴょ', 'フィ', 'ぴゃ', 'びゃ', 'ツォ',
#              ]
checked = []
# checked = hiragana
counted = {}


if __name__ == "__main__":
    """
    del        : 删除当前词汇
    show       : 显示待考察词汇
    checked    : 显示checked词汇
    save       : 保存checked词汇到文本
    progress   : 显示当前进度
    counted    : 显示词汇计数
    """
    # print(len(hiragana))
    # print(len(katakana))
    # print(len(nomaji))
    # print(len(checked))

    dict = {}
    for i in range(len(hiragana)):
        dict[hiragana[i]] = nomaji[i]
    for i in range(len(katakana)):
        dict[katakana[i]] = nomaji[i]
    total = len(dict.keys())
    deleted = len(checked)
    print('当前进度: {0:.2f} %'.format(deleted/total*100))
    for i in range(len(checked)):
        e = checked[i]
        if e in dict:
            del dict[e]
    # print(len(dict.keys()))

    def add2checked(e):
        checked.append(e)
        del dict[e]

    while True:
        if len(dict.keys()) == 0:
            input('All clear, congratulations!')
            break
        quest = random.choice(list(dict.keys()))
        answer = dict[quest]
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + quest + Style.RESET_ALL)
        guess = input("の発音は:")
        if guess == 'del':
            if quest not in checked:
                add2checked(quest)
            print(quest + ": " + answer + " was deleted.")
        elif guess == 'show':
            print(dict)
        elif guess == 'checked':
            print(checked)
        elif guess == 'counted':
            print(counted)
        elif guess == 'progress':
            deleted = len(checked)
            total = deleted + len(dict.keys())
            print('当前进度: {0:.2f} %'.format(deleted/total*100))
        elif guess == 'save':
            with open('checked.txt', 'w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                elements_per_row = 10
                for i in range(0, len(checked), elements_per_row):
                    writer.writerow(
                        [f"'{el}'" for el in checked[i:i+elements_per_row]])
            print("saved to checked.txt")
        elif guess != answer:
            print(Fore.RED + "wrong!    " +
                  Fore.CYAN + f"{quest}" +
                  Fore.WHITE + " の発音は: " +
                  Fore.CYAN + answer +
                  Fore.WHITE + " です"
                  )
            counted[quest] = 0  # 错误一次计数归零
        else:
            print(Fore.GREEN + "right!")  # 正确三次以上不再考察
            if quest not in counted:
                counted[quest] = 1
            else:
                counted[quest] += 1
            if counted[quest] >= 2:
                add2checked(quest)
                print(quest + ": " + answer + " was deleted.")
        print(Style.RESET_ALL)
