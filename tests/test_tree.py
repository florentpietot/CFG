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
        self.node = "node"
        self.children = ["child1", "child2", "child3"]
        self.tree = Tree(self.node, self.children)

    def test_node(self):
        assertIsEqual(
