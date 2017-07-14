# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for parse.py module
"""

import unittest
from nlp.tree import Tree
from nlp.parse import TopDownParser
from nlp.grammar import Grammar, Production

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


class TestExpandTree(unittest.TestCase):

    def setUp(self):
        self.parser = TopDownParser(Grammar("S", []))

    def test_expand_start_tree(self):
        """ Expand a tree with only the starting point """
        self.tree = Tree("S", [])
        self.frontier = []
        self.production = Production("S", ["NP", "VP"])
        res = (Tree("S", ["NP", "VP"]), [(0, ), (1, )])
        self.assertEqual(res, self.parser.expand_tree(self.tree, self.frontier,
                                                      self.production))

    def test_expand_tree(self):
        self.tree = Tree("S", ["NP", "VP"])
        self.frontier = [(0, ), (1, )]
        self.production = Production("NP", ["D", "N"])
        res_tree = Tree("S", [Tree("NP", ["D", "N"]), "VP"])
        res_frontier = [(0, 0), (0, 1), (1, )]
        res = (res_tree, res_frontier)
        self.assertEqual(res, self.parser.expand_tree(self.tree, self.frontier,
                                                      self.production))


class Test_ExpandTree(unittest.TestCase):

    def setUp(self):
        grammar_as_string = """
            NP -> N | D N
            N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
            D -> 'the'
        """
        grammar = Grammar.parse_grammar(grammar_as_string)
        self.parser = TopDownParser(grammar)

    def test_expand_start_tree(self):
        self.tree = Tree("NP", [])
        self.frontier = []
        res_trees = [Tree("NP", ["N"]), Tree("NP", ["D", "N"])]
        res_frontiers = [[(0, )], [(0, ), (1, )]]
        res = (res_trees, res_frontiers)
        trees, frontiers = next(self.parser._expand_tree(self.tree,
                                                         self.frontier))
        self.assertListEqual(res_trees, trees, "Trees are not equal")
        self.assertListEqual(res_frontiers, frontiers, "Frontiers are not \
                             equal")

    def test_expand_tree(self):
        self.tree = Tree("NP", ["D", "N"])
        self.frontier = [(0, ), (1, )]
        res_trees = [Tree("NP", [Tree("D", ["'the'"]), "N"])]
        res_frontiers = [[(0, 0), (1, )]]
        trees, frontiers = next(self.parser._expand_tree(self.tree,
                                                         self.frontier))
        self.assertListEqual(res_trees, trees, "Trees are not equal")
        self.assertListEqual(res_frontiers, frontiers, "Frontiers are not\
                             equal")


if __name__ == "__main__":
    unittest.main()
