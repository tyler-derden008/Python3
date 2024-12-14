#!/usr/bin/env python3
# -*- coding: utf-8 -*-

words = ["жизненный", "шикарный", "шыринка", "зажыгалка", "жестяной", "жираф", "шыроченный"]
def check_ji_shi(words):
    incorrect_words = []
    for word in words:
        if "шы" in word or "жы" in word:
            incorrect_words.append(word)
    return incorrect_words
incorrect_words = check_ji_shi(words)
if incorrect_words:
    print("Неправильно написанные слова:", incorrect_words)
else:
    print("Все слова написаны правильно.")
