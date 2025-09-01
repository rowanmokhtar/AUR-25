#!/usr/bin/env python3
import re
def count_words(sentence: str, case_sensitive: bool = False):
    word_count_dict = {}
    word = sentence.split()
    words= re.findall(r"\b\w+\b", sentence) #to remove punctuation

    for word in words:
       if not case_sensitive:
          word =word.lower()
       try:
           word_count_dict[word] += 1
           
       except KeyError:
          word_count_dict[word] = 1
          
    return word_count_dict