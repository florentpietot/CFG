# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for grammar.py module
"""

import unittest
from nlp.grammar import Production, Grammar

class TestProduction(unittest.TestCase):

    def setUp(self):
        self.production = Production("foo", "bar")

    def test_lhs(self):
        self.assertEqual("foo", self.production.lhs())

    def test_rhs(self):
        self.assertEqual("bar", self.production.rhs())

    def test_parse_production(self):
        line = "NP -> N | D N | Adj N | D Adj N"
        res = [
            Production("NP", "N"),
            Production("NP", "D N"),
            Production("NP", "Adj N"),
            Production("NP", "D Adj N")
        ]
        self.assertEqual(Production._parse_production(line), res)


class TestParseGrammar(unittest.TestCase):

    def test_error_if_input_is_not_a_string(self):
        """ Should error if input is not a string """
        input = 3
        self.assertRaises(AssertionError, Grammar.parse_grammar, input)


if __name__ == "__main__":
    unittest.main()
