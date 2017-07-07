# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for grammar.py module
"""

import unittest
from nlp.grammar import Production, Grammar

class TestProduction(unittest.TestCase):

    def setUp(self):
        # TODO: create an array of productions for testing
        self.lhs = "S"
        self.rhs = ["NP", "VP"]
        self.production = Production(self.lhs, self.rhs)

    def test_lhs(self):
        res = self.lhs
        self.assertEqual(res, self.production.lhs())

    def test_rhs(self):
        res = ("NP", "VP")
        self.assertEqual(res, self.production.rhs())

    def test_str(self):
        #TODO: handle terminals
        res = "S -> NP VP"
        self.assertEqual(res, str(self.production))

class TestParseProduction(unittest.TestCase):

    def setUp(self):
        self.lines = []
        self.lines.append("NP -> N | D N | Adj N | D Adj N")
        self.lines.append("N -> 'foo' | 'bar'")

    def test_parse(self):
        self.res = []
        res = [
            Production("NP", ["N"]),
            Production("NP", ["D", "N"]),
            Production("NP", ["Adj", "N"]),
            Production("NP", ["D", "Adj", "N"])
        ]
        self.res.append(res)
        res = [
            Production("N", ["'foo'"]),
            Production("N", ["'bar'"])
        ]
        self.res.append(res)
        for line, res in zip(self.lines, self.res):
            self.assertCountEqual(res, Production._parse_production(line))

class TestParseGrammar(unittest.TestCase):

    def test_error_if_input_is_not_a_string(self):
        """ Should error if input is not a string """
        input = 3
        self.assertRaises(AssertionError, Grammar.parse_grammar, input)


if __name__ == "__main__":
    unittest.main()
