# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Basic tree model we will use for parsing sentences given a ``grammar``
"""

from nlp.tokenize import tokenize

class Tree(list):
    """ Tree model for building a tree of productions
        Each node is a production
    """

    def __init__(self, node, children=None):
        self._node = node
        # TODO: not sure this is the better way
        if children:
            self._children = tuple(children)
            list.__init__(self, children)
        else:
            list.__init__(self, [])

    def node(self):
        """ Returns the root node of this ``Tree``
        """
        return self._node

    def children(self):
        # TODO: maybe remove?
        """ Returns the children of this ``Tree``
        """
        return self._children

    def __str__(self):
        """ Returns a verbose representation of this ``Tree`` as a string
        """
        string = "(%s" % self._node
        if len(self) > 0:
            for child in self:
                string += ", "
                string += "%s" % str(child)
        string += ")"
        # if self._children:
        #     for child in self._children:
        #         string += ", "
        #         string += "%s" % str(child)
        # string += ")"
        return string

    def __repr__(self):
        """ Returns a concise representation of this ``Tree`` as a string
        """
        return "(%r, %r)" % (self._node, tuple(self))

    def __eq__(self, other):
        """ Return True if this ``Tree`` is equal to ``other``.
        """
        return (type(self) == type(other) and
               self._node  == other._node and
               list(self) == list(other))

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
        if self:
            for child in self:
                if isinstance(child, Tree):
                    leaves += child.leaves()
                else:
                    leaves.append(child)
        else:
            leaves.append(self._node)
        return leaves


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
    trees = []
    for production in grammar.productions(lhs=grammar.start()):
        children = []
        for rhs in production.rhs():
            sub_prod = grammar.productions(lhs=rhs)
        tree = Tree(node=production.lhs, children=Tree())
        res = Tree("S",
                   children=[
                       Tree("NP", children=["N", ["D N"]]),
                       Tree("VP", children="V")])
    return tree


def subtree_for_production(production, grammar):
    """ Recursively build subtrees for a given production
    """
    # children = []
    # for rhs in production.rhs():
    #     # get list of expansions
    #     productions = grammar.productions(lhs=rhs) ## <- list
    #     children.append(subtree_for_production())
    return Tree(node=production.lhs(),
                children=[subtree_for_production(production) for production in
                          grammar.productions(lhs=production.rhs())])

def tree_for_children(grammar, production):
    for rhs in production.rhs():
        pass

def recursive_tree_from_production(production):
    pass

def recursive_tree_from_start(grammar):

    pass

def tree_from_production(production):
    """ Returns a tree from a ``production``
    """
    return Tree(node=production.lhs(), children=production.rhs())
