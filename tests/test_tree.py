# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for tree.py module
"""

import unittest
from nlp.tree import Tree
from nlp.grammar import Production

class TestTree(unittest.TestCase):
    """ Basic tests for instantiation
    """

    def setUp(self):
        self.node = "root_node"
        self.children = [Tree("child1"), Tree("child2"), Tree("child3")]
        self.tree = Tree(node=self.node, children=self.children)

    def test_node(self):
        res = self.node
        self.assertEqual(res, self.tree.node(), "Should return the root node \
                      of the tree")

    def test_children(self):
        res = self.children
        self.assertEqual(res, self.tree.children(), "Should return \
                         the children of the tree")

    def test_str_is_string(self):
        self.assertIsInstance(str(self.tree), str, msg="String expected")

    def test_str(self):
        # TODO: change this, this is bad
        res = "root_node\n\tchild1\n\tchild2\n\tchild3"
        self.assertEqual(res, str(self.tree))

    def test_repr_is_string(self):
        self.assertIsInstance(repr(self.tree), str, msg="String expected")

    def test_repr(self):
        res = "(%r, %r)" % (self.node, self.children)
        self.assertEqual(res, repr(self.tree))


class TestLeaves(unittest.TestCase):
    """ tests for the leaves() function
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

# class TestAddChild(unittest.TestCase):
#     """ Tests for the add_child function
#     """

#     def setUp(self):
#         self.node = "root_node"
#         self.children = ["child1", "child2", "child3"]
#         self.tree = Tree(self.node)

#     def test_add_child(self):
#         child = "child"
#         self.tree.add_child(child)


class TestTreeFromString(unittest.TestCase):
    pass


if  __name__ == "__main__":
    unittest.main()
