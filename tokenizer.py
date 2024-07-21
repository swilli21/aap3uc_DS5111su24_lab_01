#!/usr/bin/env python
# coding: utf-8


# Week 3 Lab : python counter, cleaner, tokenizer

'''
Functions
- clean_text, should take a string, and should return all lowercase words, and throw out any punctuation
- tokenize, should take a string and return a python list, where each item is a word in the file
- count_words, should take a string and return a dictionary with the words as keys, and their counts as value
'''


from collections import Counter
import string
import re
from string import punctuation


def clean_text(data):


    '''
    take a string and return all lower case words, remove punctuations

    '''
    assert isinstance(data, str), f"input should be a string type {type(data)} received instead"

    trans = str.maketrans('', '', string.punctuation)

    data = data.lower().translate(trans)

    assert isinstance(data, str) , "data should be a string data type"
    assert not clean_text == "", "this string should not be empty"
    return data



def tokenize(data):
    '''take a string and return a python list, where each item is a word in the file'''
    assert isinstance(data, str), f"input should be a string type {type(data)} received instead"

    tokens = clean_text(data).split() # call previous function

    assert isinstance(tokens, list), f"should be a list ,type {type(data)} received instead"
    return tokens


def count_words(data):
    '''should take a string and return a dictionary with the words as keys, and their counts as value'''
    counts = Counter(tokenize(clean_text(data)))

    assert isinstance(data, str), f"input should be a string type {type(data)} received instead"

    assert isinstance(counts, dict), f"should be a dict ,type {type(data)} received instead"
    print("Count words was called")
    return counts
#TEST
def test_tokenize():

    assert tokenize("a b c") == ['a', 'b', 'c']

if __name__=="__main__":

    data =  '''A man of genius usually gains a footing with the success of some one effort, and this is not always his greatest. Recognition is the more
    instant for having been postponed. He does not acquire it, like a miser's fortune, coin after coin, but "not at all or all in all." '''
    clean_text(data)
    tokenize(data)
    count_words(data)
