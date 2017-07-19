
# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

def tokenize(string):
    """ Basic implementation of tokenizing a string
        Given a string, returns a list containing all words of the string
        Current implementation is incomplete, it should strip any punctuation,
        etc..
        Args:
            string(str): string to tokenize
        Return:
            token(list): list of words as ``strings``

        Example:
            "Fall leaves fall" -> ["fall", "leaves", "fall"]
    """
    if len(string) > 0 and string[-1] == '.':
        string = string[:-1]
    tokens = string.lower().split()
    return tokens
