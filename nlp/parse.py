# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Parse sentences using trees
"""

from nlp.tree import Tree, tree_from_production
from nlp.grammar import Grammar, Production

class TopDownParser(object):

    def __init__(self, grammar):
        """ params:
            grammar: a ``grammar`` object that states rules for the parsing
        """
        self._grammar = grammar

    def grammar(self):
        return self._grammar

    def parse(self, tokens):
        """ Parse a list of tokens and return the possible tree based on the
            ``grammar of this ``Parser``
        """
        tokens = list(tokens)
        root_tree = Tree(self._grammar.start(), [])
        frontier = root_tree
        return self._parse(tokens, root_tree, frontier)

    def _parse(self, tokens, initial_tree, frontier):
        # TODO: improve this docstring
        """ Recursively parse a list of tokens given a starting tree and a
            frontier of "to be expanded" nodes
            Args:
                tokens: ``list`` if strings we want to match to a derivation
                initial_tree: starting ``tree``
                frontier: ``list`` of candidates for expansion?
        """
        if len(frontier) == 0:
            # TODO:
            yield "TODO"
        elif isinstance(frontier[0], Tree):
            production = self.grammar().productions(lhs=frontier[0])
            frontier = initial_tree.leaves()
            self._expand(initial_tree, frontier[0])
        # elif len(frontier) == 0:
        #     yield tree

    def _expand_tree(self, tree, frontier):
        print(tree)
        print(frontier)
        # for production in self.grammar.productions(lhs=frontier):
        #     print(production)
        #     subtree = tree_from_production(production)
        #     print(subtree)

    def expand_tree(self, tree, frontier):
        """ Generator function: recursively expand a tree
            Args:
                tree: the ``tree`` to expand
                frontier: a ``list`` of node candidate to expand
        """
        # Take first element of frontier
        # frontier[0]



