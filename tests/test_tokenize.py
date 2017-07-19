# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for tokenize module
"""

import unittest
from nlp.tokenize import tokenize

class TestTokenize(unittest.TestCase):

    def setUp(self):
        self.string = "Fall leaves fall"

    def test_returns_empty_list(self):
        self.assertIsInstance(tokenize(""), list)
        self.assertEqual(tokenize(""), [])

    def test_returns_a_list(self):
        self.assertIsInstance(tokenize(self.string), list,
                              msg="It should return a ``list``")

    def test_returns_list_of_words(self):
        res = ["fall", "leaves", "fall"]
        self.assertEqual(res, tokenize(self.string),
                        msg="It should return list of words")

    def test_removes_dot_at_end_of_sentence(self):
        res = ["fall", "leaves", "fall"]
        self.string += "."
        self.assertEqual(res, tokenize(self.string),
                        msg="It should remove the dot")


if __name__ == "__main__":
    unittest.main()
