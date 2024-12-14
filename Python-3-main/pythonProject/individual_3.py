#!/usr/bin/env python3
# -*- coding: utf-8 -*-

words = ["мир.", "сила.", "интеллект.", "разум.", "силовик."]
def insert_letter_after_i(words, letter):
    modified_words = []
    for word in words:
        index = word.find('и')
        if index != -1 and index < len(word) - 1:
            modified_word = word[:index + 1] + letter + word[index + 1:]
            modified_words.append(modified_word)
        else:
            modified_words.append(word)
    return modified_words
letter_to_insert = 'x'
modified_words = insert_letter_after_i(words, letter_to_insert)
print(modified_words)
