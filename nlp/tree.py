# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Basic tree model we will use for parsing sentences given a ``grammar``
"""

class Tree(list):
    """ Tree model for building a tree of productions
        Each node is a production
    """

    def __init__(self, node=None, children=None):
        self._node = node
        self._children = childen

    def node(self):
        return self._node

    def children(self):
        return self._children

    def leaves(self):
        """ Returns the leaves of the tree
        """
        pass

    def make_node(self, children=None):
        pass

    def add_child(self, node, child):
        pass

    @classmethod
    def make_tree_from_production(self, production):
        pass

