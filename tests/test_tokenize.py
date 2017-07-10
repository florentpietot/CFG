# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for tokenize module
"""

import unittest
from nlp.tokenizer import tokenize

class TestTokenize(unittest.TestCase):

    def setUp(self):
        self.string = "Fall leaves fall"

    def test_return_if_empty_string(self):
        """ Should returns empty list
        """
        self.assertEqual([], tokenize(""))

    def test_return_list(self):
        self.assertIsInstance(tokenize(self.string), list,
                              msg="Should return a list")

    def test_tokenize(self):
        res = ["fall", "leaves", "fall"]
        self.assertEqual(res, tokenize(self.string))


if __name__ == "__main__":
    unittest.main()
