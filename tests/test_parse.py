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


# class TestParse(TestTopDownParserInit):

#     def setUp(self):
#         grammar_as_string = """
#         S -> NP VP
#         NP -> N | D N | Adj N | D Adj N
#         VP -> V NP | V | V NP NP
#         N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
#         V -> 'spring' | 'leaves' | 'fall' | 'left'
#         D -> 'the'
#         Adj -> 'fall' | 'spring' | 'purple' | 'left'
#         """
#         self.grammar = Grammar.parse_grammar(grammar_as_string)
#         self.parser = TopDownParser(self.grammar)
#         self.tokens = ["fall", "leaves", "fall"]

#     def test_parse(self):
#         parse_1 = Tree("S",
#                        [Tree("NP", [Tree("N", ["'fall'"])]),
#                         Tree("VP", [Tree("V", ["'leaves'"]), Tree("N",
#                                                                   ["'fall'"])])])
#         parse_2 = Tree("S",
#                        [Tree("NP", [Tree("Adj", ["'fall'"]),
#                                     Tree("N",["'leaves'"])]),
#                        Tree("VP", [Tree("V", ["'fall'"])])])
#         res = [parse_1, parse_2]
#         self.assertListEqual(res, self.parser.parse(self.tokens))


class TestExpandTree(unittest.TestCase):

    def setUp(self):
        self.parser = TopDownParser(Grammar("S", []))

    def test_expand_start_tree(self):
        """ Expand a tree with only the starting point """
        self.tree = Tree("S", [])
        self.frontier = []
        self.production = Production("S", ["NP", "VP"])
        res_tree = Tree("S", [Tree("NP", []), Tree("VP", [])])
        res_frontier = [(0, ), (1, )]
        res = (res_tree, res_frontier)
        self.assertEqual(res, self.parser.expand_tree(self.tree, self.frontier,
                                                      self.production))

    def test_expand_tree(self):
        self.tree = Tree("S", ["NP", "VP"])
        self.frontier = [(0, ), (1, )]
        self.production = Production("NP", ["D", "N"])
        res_tree = Tree("S", [Tree("NP", [Tree("D", []), Tree("N", [])]), "VP"])
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
        """ Expand a tree with only the top node """
        self.tree = Tree("NP", [])
        self.frontier = []
        res_trees = [Tree("NP", [Tree("N", [])]),
                     Tree("NP", [Tree("D", []), Tree("N", [])])]
        res_frontiers = [[(0, )], [(0, ), (1, )]]
        res = (res_trees, res_frontiers)
        trees, frontiers = self.parser._expand_tree(self.tree, self.frontier)
        self.assertListEqual(res_trees, trees, "Trees are not equal")
        self.assertListEqual(res_frontiers, frontiers, "Frontiers are not \
                             equal")

    def test_expand_tree(self):
        """ Expand a tree """
        self.tree = Tree("NP", [Tree("D", []), Tree("N", [])])
        self.frontier = [(0, ), (1, )]
        res_trees = [Tree("NP", [Tree("D", ["'the'"]), Tree("N", [])])]
        res_frontiers = [[(0, 0), (1, )]]
        trees, frontiers = self.parser._expand_tree(self.tree, self.frontier)
        self.assertListEqual(res_trees, trees, "Trees are not equal")
        self.assertListEqual(res_frontiers, frontiers, "Frontiers are not\
                             equal")

    def test_expand_non_expandable(self):
        """ Expand a tree where the frontier is not an expandable node
            It should return the same tree and the frontier without first
            element
        """
        self.tree = Tree("NP", [Tree("D", ["'the'"]), Tree("N", [])])
        self.frontier = [(0, 0), (1, )]
        res_trees = [self.tree]
        res_frontiers = [[(1, )]]
        trees, frontiers = self.parser._expand_tree(self.tree, self.frontier)
        self.assertListEqual(res_trees, trees, "Trees should be the same")
        self.assertListEqual(res_frontiers, frontiers, "Frontiers should be \
                             the same")


if __name__ == "__main__":
    unittest.main()
