# -*- coding: utf-8 -*-
import os
import csv
import random
from colorama import Fore, Style
import re
import pickle
import pandas as pd


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == '__main__':
    trie = Trie()

    # 插入一些字符串
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("orange")
    trie.insert("grape")
    trie.insert("pear")

    # 搜索存在的字符串
    print(trie.search("apple"))  # 输出: True
    print(trie.search("banana"))  # 输出: True

    # 搜索不存在的字符串
    print(trie.search("kiwi"))  # 输出: False
    print(trie.search("peach"))  # 输出: False

    # 判断前缀是否存在
    print(trie.starts_with("app"))  # 输出: True
    print(trie.starts_with("ban"))  # 输出: True
    print(trie.starts_with("ora"))  # 输出: True
    print(trie.starts_with("gr"))  # 输出: True
    print(trie.starts_with("pea"))  # 输出: True

    # 判断不存在的前缀
    print(trie.starts_with("ki"))  # 输出: False
    print(trie.starts_with("peach"))  # 输出: False
