# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:22:40 2022

@author: User
"""

import random
from uzwords import words

def det_wort():
    word = random.choive(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters():
            display_letter += "-"
        return display_letter

def play():
    
    word = get_word()
    
    user_letters = ''
    print(f"Men {len(word)} xonali son o'yladim. Topa olasimi?")
    
    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"SHu vaqgacha kiritga xariflaringiz: {user_letters}")
            
        letter = input("xarif kiriting: ").upper()
        if letter in user_letters:
            print("Bu xarifni aval kiritgansiz. Boshqa xarif kiriting.")
            continue
        elif letter in word:
            word_letter.remove(letter)
            print(f"{letter} xarfi to'g'ri.")
        else:
            print("Bunday xarif yuq.")
        user_letters += letter
    print(f"Tabreklayman! {word} so'zni {len(user_letters)} ta urunishda tobdingiz.")