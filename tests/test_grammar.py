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

    # def test_parse_production(self):
    #     #TODO:
    #     pass
    #     line = "NP -> N | D N | Adj N | D Adj N"
    #     res = [
    #         Production("NP", "N"),
    #         Production("NP", "D N"),
    #         Production("NP", "Adj N"),
    #         Production("NP", "D Adj N")
    #     ]
    #     self.assertEqual(Production._parse_production(line), res)

class TestParseProduction(unittest.TestCase):

    def setUp(self):
        self.line = "NP -> N | D N | Adj N | D Adj N"

    def test_parse(self):
        res = [
            Production("NP", ["N"]),
            Production("NP", ["D", "N"]),
            Production("NP", ["Adj", "N"]),
            Production("NP", ["D", "Adj", "N"])
        ]
        self.assertCountEqual(res, Production._parse_production(self.line))


class TestParseGrammar(unittest.TestCase):

    def test_error_if_input_is_not_a_string(self):
        """ Should error if input is not a string """
        input = 3
        self.assertRaises(AssertionError, Grammar.parse_grammar, input)


if __name__ == "__main__":
    unittest.main()
