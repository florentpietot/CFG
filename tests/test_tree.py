# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for tree.py module
"""

import unittest
from nlp.tree import (Tree, tree_from_string, tree_from_production)
from nlp.grammar import Production, Grammar

class TestTree(unittest.TestCase):
    """ Basic tests for instantiation of ``tree``
    """

    def setUp(self):
        self.node = "root_node"
        self.child_1 = Tree(node="child_1", children=["grandchild_1",
                                                      "grandchild_2",
                                                      "grandchild_3"])
        self.child_2 = Tree(node="child_2")
        self.child_3 = "child_3"
        self.children = [self.child_1, self.child_2, self.child_3]
        self.tree = Tree(node=self.node, children=self.children)

    def test_node(self):
        res = self.node
        self.assertEqual(res, self.tree.node(), "Should return the root node \
                      of the tree")

    def test_children(self):
        res = tuple(self.children)
        self.assertEqual(res, self.tree.children(), "Should return \
                         the children of the tree")

    def test_str_is_string(self):
        self.assertIsInstance(str(self.tree), str, msg="String expected")

    def test_str(self):
        # TODO: change this, this is bad
        res = "(root_node, (child_1, grandchild_1, grandchild_2, grandchild_3), (child_2), child_3)"
        self.assertEqual(res, str(self.tree))

    def test_repr_is_string(self):
        self.assertIsInstance(repr(self.tree), str, msg="String expected")

    def test_repr(self):
        res = "(%r, %r)" % (self.node, tuple(self.children))
        self.assertEqual(res, repr(self.tree))

    def test_copy(self):
        copy = self.tree.copy()
        self.assertEqual(copy, self.tree, "Copy should be equal")

    def test_len(self):
        res = 3
        self.assertEqual(res, len(self.tree), "Lenght of tree should be equal to 6")

class TestGetItem(unittest.TestCase):
    """ Test case for __getitem__
    """

    def setUp(self):
        self.node = "node"
        self.child_1 = Tree(node="child_1", children=["grandchild_1",
                                                "grandchild_2",
                                                "grandchild_3"])
        self.child_2 = Tree(node="child_2")
        self.child_3 = "child_3"
        self.tree = Tree(node=self.node, children=[self.child_1, self.child_2,
                                                   self.child_3])
    def test_get_no_index(self):
        """ Test for when index is empty tuple/array """
        res = self.tree
        self.assertEqual(res, self.tree[[]], "Should return original tree")
        self.assertEqual(res, self.tree[()], "Should return original tree")

    def test_get_first_child(self):
        """ Should get first child by calling self.tree[0] """
        res = self.child_1
        self.assertEqual(res, self.tree[0], "Didn't get first child")

    def test_get_second_grandchild(self):
        """ Should get grandchild_2 by calling
            self.tree[(0, 1)] or self.tree[[0, 1]]
        """
        res = "grandchild_2"
        self.assertEqual(res, self.tree[(0, 1)])
        self.assertEqual(res, self.tree[[0, 1]])

class TestSetItems(unittest.TestCase):
    """ Test __setitem__ for our ``tree`` class
    """

    def setUp(self):
        self.tree = Tree("S", [Tree("NP", ["D", "N"]), "VP"])
        self.new_child = Tree("VP", ["V", "N"])

    def test_set_existing(self):
        """ Test set/replace an existing node of the tree with an integer index
        """
        res = Tree("S", [Tree("NP", ["D", "N"]), self.new_child])
        self.tree[1] = self.new_child
        self.assertEqual(res, self.tree)

    def test_set_tuple(self):
        """ Test with a tuple of length > 1 """
        res = Tree("S", [Tree("NP", ["D", self.new_child]), "VP"])
        index = (0, 1)
        self.tree[index] = self.new_child
        self.assertEqual(res, self.tree)

    def test_set_array(self):
        """ Test with a list of length > 1 """
        res = Tree("S", [Tree("NP", ["D", self.new_child]), "VP"])
        index = [0, 1]
        self.tree[index] = self.new_child
        self.assertEqual(res, self.tree)

    # def test_set_empty_index(self):
    #     """ Test when the index is an empty array or tuple """
    #     index = []
    #     self.tree[index] = self.new_child


class TestLeaves(unittest.TestCase):
    """ Test case for getting the leaves from a ``tree``
    """

    def setUp(self):
        self.node = "node"
        self.child_1 = Tree(node="child_1", children=["grandchild1-1",
                                                "grandchild1-2",
                                                "grandchild1-3"])
        self.child_2 = Tree(node="child_2")
        self.child_3 = "child_3"
        self.tree = Tree(node=self.node, children=[self.child_1, self.child_2,
                                                   self.child_3])

    def test_leaves(self):
        res = []
        # TODO: improve this (better flattening of all lists)
        res += self.child_1.children()
        res.append(self.child_2.node())
        res.append(self.child_3)
        self.assertEqual(res, self.tree.leaves())


class TestAddChild(unittest.TestCase):
    pass


class TestTreeFromString(unittest.TestCase):
    pass


class TestTreeFromProduction(unittest.TestCase):
    """ Test case for creating trees from ``production``
    """

    def setUp(self):
        self.production = Production("S", ["NP", "VP"])

    def test_tree_from_production(self):
        res = Tree("S", [Tree("NP", []), Tree("VP", [])])
        self.assertEqual(res, tree_from_production(self.production))

    def test_tree_from_production_with_terminal(self):
        self.production = Production("N", ["'fall'"])
        res = Tree("N", ["'fall'"])
        self.assertEqual(res, tree_from_production(self.production))

class TestTreeFromGrammar(unittest.TestCase):
    """ Test case for creating trees from ``grammar``
    """

    def setUp(self):
        grammar_as_string = """
            S -> NP VP
            NP -> N
            VP -> V NP | V
            N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
            V -> 'spring' | 'leaves' | 'fall' | 'left'
        """
        self.grammar = Grammar.parse_grammar(grammar_as_string)


class TestSubtreeFromProduction(unittest.TestCase):

    def setUp(self):
        productions = [
            Production("S", ["NP", "VP"]),
            Production("NP", ["N"]),
            Production("NP", ["D", "N"]),
            Production("VP", ["V"]),
            Production("VP", ["V", "N"])
        ]
        self.grammar = Grammar("S", productions)

    def test_subtree_from_production(self):
        # get a random start production
        res = Tree("S", children=[
            Tree("NP", children=["N", ["D N"]]),
            Tree("VP", children="V")])
        start_prod = self.grammar.productions(self.grammar.start())[0]


if  __name__ == "__main__":
    unittest.main()
