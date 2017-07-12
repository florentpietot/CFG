# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for grammar.py module
"""

import unittest
import copy
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

    def test_eq(self):
        """ Test equality """
        other = copy.copy(self.production)
        self.assertEqual(self.production, other)

    def test_ne(self):
        """ Test inequality """
        other = Production("NP", ["N"])

class TestParseProduction(unittest.TestCase):

    def setUp(self):
        self.line = "Adj -> 'fall' | 'spring' | 'purple' | 'left'"

    def test_return_array(self):
        """ Make sure it returns an array """
        self.assertIsInstance(Production._parse_production(self.line),
                              list)

    def test_parse(self):
        """ Should work properly on valid data """
        res = [
            Production("Adj", ["'fall'"]),
            Production("Adj", ["'spring'"]),
            Production("Adj", ["'purple'"]),
            Production("Adj", ["'left'"])
        ]
        self.assertEqual(res, Production._parse_production(self.line))


class TestGrammar(unittest.TestCase):

    def setUp(self):
        self.start = "NP"
        self.productions = [
            Production("NP", ["N"]),
            Production("NP", ["D", "N"])
        ]
        self.grammar = Grammar(self.start, self.productions)

    def test_str(self):
        """ Should return the verbose representation of the ``grammar`` as a
        string
        """
        res = ("Grammar starting with: \"%s\"\n2 productions:\nNP -> N\nNP -> D N"
               % (self.grammar.start()))
        self.assertEqual(res, str(self.grammar))

    def test_repr(self):
        """ Should return the concise representation of the ``grammar``as a
        string
        """
        res = "Grammar with 2 productions starting with \"NP\""
        self.assertEqual(res, repr(self.grammar))


class TestGrammarProductions(unittest.TestCase):
    """ Test case for the productions(self, lhs=None)
    This should returns the ``productions`` of the ``grammar``
    filtered by left-hand side
    """

    def setUp(self):
        self.productions = [
            Production("NP", ["N"]),
            Production("NP", ["D", "N"]),
            Production("N", ["'fall'"]),
            Production("N", ["'spring'"]),
            Production("N", ["'leaves'"]),
            Production("N", ["'dog'"]),
            Production("N", ["'cat'"]),
            Production("D", ["'the'"])
        ]
        self.grammar = Grammar("NP", self.productions)

    def test_lhs_is_none(self):
        res = self.productions
        self.assertIsInstance(self.grammar.productions(), list)
        self.assertEqual(res, self.grammar.productions(),
                         msg=("Should return all ``productions``\
                              of this``grammar``"))


    def test_standard_use_case(self):
        res = self.productions[:2]
        self.assertIsInstance(self.grammar.productions(lhs="NP"), list)
        self.assertCountEqual(res, self.grammar.productions(lhs="NP"))


class TestGrammarCalculateIndexes(unittest.TestCase):

    def setUp(self):
        self.start = "NP"
        self.productions = [
            Production("NP", ["N"]),
            Production("NP", ["D", "N"]),
            Production("N", ["'fall'"]),
            Production("N", ["'spring'"]),
            Production("N", ["'leaves'"]),
            Production("D", ["'the'"])
        ]
        self.grammar = Grammar(self.start, self.productions)

    def test_calculate_lhs_indexes(self):
        # TODO: no idea on how to test this
        """ We'll just check that this ``grammar``._lhs_index is properly set
        after init
        """
        res = {}
        res["NP"] = [
            Production("NP", ["N"]),
            Production("NP", ["D", "N"])
        ]
        res["N"] = [
            Production("N", ["'fall'"]),
            Production("N", ["'spring'"]),
            Production("N", ["'leaves'"])
        ]
        res["D"] = [
            Production("D", ["'the'"])
        ]
        self.assertEqual(res, self.grammar._calculate_lhs_index())


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

    def test_return_grammar_object(self):
        """ parse_grammar should return an array
        """
        self.assertIsInstance(Grammar.parse_grammar(self.grammar_as_string),
                              Grammar)

    def test_parse_grammar(self):
        # TODO: define __eq__ for Grammar object so we can test equality
        """ Test that the string representation of a grammar obtained using
        parse_grammar is equal to one created with constructor.
        """
        start = "NP"
        productions = [
            Production("NP", ["N"]),
            Production("NP", ["D", "N"]),
            Production("N", ["'fall'"]),
            Production("N", ["'spring'"]),
            Production("N", ["'leaves'"]),
            Production("N", ["'dog'"]),
            Production("N", ["'cat'"]),
            Production("D", ["'the'"])
        ]
        res = Grammar(start, productions)
        self.assertEqual(str(res),
                         str(Grammar.parse_grammar(self.grammar_as_string)))




if __name__ == "__main__":
    unittest.main()
