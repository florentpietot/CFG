# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for parse.py module
"""

import unittest
from nlp.parse import TopDownParser
from nlp.grammar import Grammar


class TestTopDownParserInit(unittest.TestCase):
    """ Init tests """

    def setUp(self):
        grammar_as_string = """
        NP -> N | D N
        N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
        D -> 'the'
        """
        self.grammar = Grammar.parse_grammar(grammar_as_string)
        self.parser = TopDownParser(self.grammar)

    def test_grammar(self):
        """ Check it returns the ``grammar`` param properly """
        res = self.parser.grammar()
        self.assertEqual(res, self.parser.grammar(),
                        "It should return the grammar")


class TestParse(TestTopDownParserInit):

    def setUp(self):
        grammar_as_string = """
        NP -> N | D N
        N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
        D -> 'the'
        """
        self.grammar = Grammar.parse_grammar(grammar_as_string)
        self.parser = TopDownParser(self.grammar)
        self.tokens = ["fall", "leaves", "fall"]

    def test_parse(self):
        self.parser.parse(self.tokens)


if __name__ == "__main__":
    unittest.main()
