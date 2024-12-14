#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sentence = "искусственный интеллект - большая сила, способная решить множество бытовых рутинных занятий, но с большой силой приходит и большая ответственность"
letters = []
for char in sentence:
    if char == 'м' or char == 'н':
        letters.append(char)
print(letters)
