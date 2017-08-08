# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Parse sentences using trees
"""

from cfg.tree import Tree, tree_from_production
from cfg.tokenize import tokenize


class TopDownParser(object):

    def __init__(self, grammar, verbose=0):
        """ params:
            grammar: a ``grammar`` object that states rules for the parsing
        """
        self._grammar = grammar
        self._verbose = verbose

    def grammar(self):
        return self._grammar

    def parse(self, tokens):
        """ Parse a list of tokens and return the possible tree based on the
            ``grammar of this ``Parser``
            Args:
                tokens: a string
        """
        if len(tokens) == 0:
            raise ValueError("Tokens can't be empy")

        # Tokenize if needed
        if not isinstance(tokens, list):
            tokens = tokenize(tokens)
        root_tree = Tree(self._grammar.start(), [])
        frontier = [()]
        return self._parse(tokens, root_tree, frontier)

    def _parse(self, tokens, tree, frontier):
        """ Recursively parse a list of tokens given a starting tree and a
            frontier of "to be expanded" nodes
            Args:
                tokens: ``list`` if strings we want to match to a derivation
                initial_tree: starting ``tree``
                frontier: ``list`` of candidates for expansion?
        """
        if self._verbose >= 1:
            print("Parsing: %s with frontier: %s for tokens: %s" % (tree,
                                                                    frontier,
                                                                    tokens))
        if len(tokens) == 0 and len(frontier) == 0:
            # Found a match
            yield (tree, frontier)
        elif len(tokens) == 0 or len(frontier) == 0:
            pass
        elif isinstance(tree[frontier[0]], Tree):
            # Expand the tree at frontier
            for (new_tree, new_frontier) in self._expand(tokens, tree,
                                                         frontier):
                yield (new_tree, new_frontier)
        else:
            # This is a terminal, we will match it
            for (new_tree, new_frontier) in self._match(tokens, tree,
                                                        frontier):
                yield (new_tree, new_frontier)

    def _match(self, tokens, tree, frontier):
        """ Match
        """

        if len(tokens) == 0:
            raise ValueError("`tokens` requires at least one element")
        if len(frontier) == 0:
            raise ValueError("`frontier` requires at least one element")

        if self._verbose >= 1:
            print("Matching %s with frontier %s and tokens %s" % (tree,
                                                                  frontier,
                                                                  tokens))

        # TODO: clean this dirty hack. Maybe create Terminal class?
        if len(tokens) > 0 and tree[frontier[0]][1:-1] == tokens[0]:
            newtree = tree.copy(deep=True)
            for new_tree, new_frontier in self._parse(tokens[1:], newtree,
                                                      frontier[1:]):
                yield (new_tree, new_frontier)

    def _expand(self, tokens, tree, frontier):
        """ Expand a ``tree`` with the first element of the ``frontier``
            If given a ``production``, will expand the tree following this
            production rule, otherwise, will use this ``parser.grammar()``
            production rules
        """

        if len(frontier) == 0:
            raise ValueError("Frontier requires at least one element")

        if self._verbose >= 1:
            print("Expanding %s at subtree %s" % (tree, tree[frontier[0]]))

        if isinstance(tree[frontier[0]], Tree):
            for production in self.grammar().productions():
                if tree[frontier[0]].node() == production.lhs():
                    subtree = tree_from_production(production)
                    if frontier[0] == ():
                        newtree = subtree
                    else:
                        newtree = tree.copy(deep=True)
                        newtree[frontier[0]] = subtree
                    newfrontier = [frontier[0] + (i, ) for i in
                                   range(len(production.rhs()))]
                    newfrontier = newfrontier + frontier[1:]
                    for new_tree, new_frontier in self._parse(tokens, newtree,
                                                              newfrontier):
                        yield (new_tree, new_frontier)
