# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tokenize module to tokenize a sentence into list of words

    Example:
        "Fall leaves fall" -> ["fall", "leaves", "fall"]
"""

def tokenize(string):
    """ Tokenize a string
    """
    tokens = string.lower().split()
    return tokens
