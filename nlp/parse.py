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
        frontier = []
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
        """ Expand a tree following this ``parser.grammar`` rules
            Returns all possible trees by expanding the first element of
            frontier
        """
        trees = []
        frontiers = []
        if len(frontier) > 0:
            node = tree[frontier[0]]
        else:
            node = self.grammar().start()
        for production in self.grammar().productions(lhs=node):
            new_tree, new_frontier = self.expand_tree(tree, frontier,
                                                      production)
            trees.append(new_tree)
            frontiers.append(new_frontier)
        yield (trees, frontiers)


    def expand_tree(self, tree, frontier, production):
        """ Expand a tree from first element of a frontier given a production

            Args:
                tree: the ``tree`` to be expanded
                frontier: the list of nodes candidates for expansion
                production: production rule to follow in order to expand

            Examples:
                Tree: (S, NP, NP)
                Frontier: it should be: [(0, ), (1, )]
                Production: (NP -> D N)

                Returns:
                    Tree: (S, (NP, D, N), VP)
                    Frontier: [(0, 0), (0, 1), (1, )]
        """
        subtree = tree_from_production(production)
        if len(frontier) == 0:
            new_tree = subtree
            new_frontier = [(i, ) for i in range(len(production.rhs()))]
        else:
            new_tree = tree.copy()
            new_tree[frontier[0]] = tree_from_production(production)
            new_frontier = [frontier[0] + (i, ) for i in
                            range(len(production.rhs()))]
            new_frontier = new_frontier + frontier[1:]
        return new_tree, new_frontier
