from random import choice

with open("words.txt", "r") as f:
    word_list = [word[:-1]  for word in f.readlines()]
    word_set = set(word_list)

def is_valid_word(word:str) -> bool:
    return word.lower() in word_list

def get_random_word() -> str:
    return choice(word_list).upper()