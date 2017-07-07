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
        self.lines.append("Adj -> 'fall' | 'spring' | 'purple' | 'left'")

    def test_return_array(self):
        self.assertIsInstance(Production._parse_production(self.lines[0]),
                              list)

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
            Production("Adj", ["'fall'"]),
            Production("Adj", ["'spring'"]),
            Production("Adj", ["'purple'"]),
            Production("Adj", ["'left'"])
        ]
        self.res.append(res)
        for line, res in zip(self.lines, self.res):
            self.assertCountEqual(res, Production._parse_production(line))


class TestGrammar(unittest.TestCase):

    def setUp(self):
        self.productions = [
            Production("NP", ["N"]),
            Production("NP", ["D", "N"])
        ]
        self.grammar = Grammar(self.productions)

    def test_productions_is_list(self):
        """ Should return the list of ``productions``
            as a ``list``
        """
        self.assertIsInstance(self.grammar.productions(), list)

    def test_productions(self):
        """ Should return the list of ``predictions``
        """
        self.assertEqual(self.productions, self.grammar.productions())


class TestParseGrammar(unittest.TestCase):

    def setUp(self):
        self.grammar_as_string = """
            NP -> N | D N
            N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
            D -> 'the'
        """

    def test_error_if_input_is_not_a_string(self):
        """ Should error if input is not a string """
        inputs = [-3, None, 3.4, [3, 4, 5], [], {}]
        for input in inputs:
            self.assertRaises(AssertionError, Grammar.parse_grammar, input)

    def test_return_array(self):
        """ parse_grammar should return an array
        """
        self.assertIsInstance(Grammar.parse_grammar(self.grammar_as_string),
                              list)


if __name__ == "__main__":
    unittest.main()
