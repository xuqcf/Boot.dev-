from functools import lru_cache


@lru_cache()
def is_palindrome(word):
    return word == word[::-1]
