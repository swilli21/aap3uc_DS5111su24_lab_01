"""
This module provides functions to clean text, tokenize it into words,
and count the frequency of each word.
"""

from collections import Counter
import string

def clean_text(text):
    """
    Take a string and return all lowercase words with punctuation removed.
    """
    assert isinstance(text, str), f"input should be a string type {type(text)} received instead"

    trans = str.maketrans('', '', string.punctuation)
    cleaned_text = text.lower().translate(trans)

    assert isinstance(cleaned_text, str), "cleaned_text should be a string data type"
    assert cleaned_text != "", "cleaned_text should not be empty"
    return cleaned_text

def tokenize(text):
    """
    Take a string and return a Python list, where each item is a word in the string.
    """
    assert isinstance(text, str), f"input should be a string type {type(text)} received instead"

    tokens = clean_text(text).split()  # Call previous function

    assert isinstance(tokens, list), f"should be a list, type {type(tokens)} received instead"
    return tokens

def count_words(text):
    """
    Count the words in the text.
    """
    assert isinstance(text, str), f"input should be a string type {type(text)} received instead"

    counts = Counter(tokenize(text))

    assert isinstance(counts, dict), f"should be a dict, type {type(counts)} received instead"
    print("Count words was called")
    return counts

if __name__ == "__main__":
    DATA = '''A man of genius usually gains like a miser's fortune, coin after coin'''
    clean_text(DATA)
    tokenize(DATA)
    count_words(DATA)
