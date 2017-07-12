# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Basic tree model we will use for parsing sentences given a ``grammar``
"""

from nlp.tokenize import tokenize

class Tree(object):
    """ Tree model for building a tree of productions
        Each node is a production
    """

    def __init__(self, node=None, children=None):
        self._node = node
        # TODO: not sure this is the better way
        if children:
            self._children = tuple(children)
        else:
            self._children = None

    def node(self):
        """ Returns the root node of this ``Tree``
        """
        return self._node

    def children(self):
        """ Returns the children of this ``Tree``
        """
        return self._children

    def __str__(self):
        """ Returns a verbose representation of this ``Tree`` as a string
        """
        string = "(%s" % self._node
        if self._children:
            for child in self._children:
                string += ", "
                string += "%s" % str(child)
        string += ")"
        return string

    def __repr__(self):
        """ Returns a concise representation of this ``Tree`` as a string
        """
        return "(%r, %r)" % (self._node, self._children)

    def __eq__(self, other):
        """ Return True if this ``Tree`` is equal to ``other``.
        """
        return (type(self) == type(other) and
               self._node  == other._node and
               self._children == other._children)

    def __ne__(self, other):
        """ Return True if this ``Tree`` is not equal to ``other``.
        """
        return not self == other

    def contains(self, elem):
        pass

    def leaves(self):
        """ Returns the leaves of the tree
        """
        leaves = []
        if self._children:
            for child in self._children:
                if isinstance(child, Tree):
                    leaves += child.leaves()
                else:
                    leaves.append(child)
        else:
            leaves.append(self._node)
        return leaves

    def make_node(self, children=None):
        pass

    def add_child(self, node, child):
        pass


def tree_from_string(string, grammar=None):
    """ Returns a tree from a string and a ``grammar``
    """
    if grammar is None:
        assert ValueError("Grammar param can't be none.")
    tokens = tokenize(string)
    trees = []
    token = tokens[0]
    token = "'%s'" % token
    for production in grammar.productions():
        if token in production.rhs():
            trees.append(Tree(node=production))
    return trees

def tree_from_grammar(grammar):
    """ Returns a tree given a ``grammar``
    """
    for production in grammar.productions():
        # get list of production that contains start
        pass


def tree_from_production(production):
    """ Returns a tree from a ``production``
    """
    return Tree(node=production.lhs(), children=production.rhs())
