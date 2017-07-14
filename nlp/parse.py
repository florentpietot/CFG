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
        frontier = [()]
        return self._parse(tokens, root_tree, frontier)

    def _parse(self, tokens, tree, frontier):
        # TODO: improve this docstring
        """ Recursively parse a list of tokens given a starting tree and a
            frontier of "to be expanded" nodes
            Args:
                tokens: ``list`` if strings we want to match to a derivation
                initial_tree: starting ``tree``
                frontier: ``list`` of candidates for expansion?
        """
        print("Parsing: %s with frontier: %s for tokens: %s" % (tree,
                                                                frontier,
                                                                tokens))
        if len(tokens) == 0 and len(frontier) == 0:
            # Found a match
            print("Match: %s" % tree)
            yield tree
        elif len(frontier) == 0:
            print("failed")
        else:
            if isinstance(tree[frontier[0]], Tree):
                # Expand the tree at frontier
                print("Expanding tree: %s" % tree[frontier[0]])
                new_trees, new_frontiers = self._expand_tree(tree, frontier)
                for new_tree, new_frontier in zip(new_trees, new_frontiers):
                    # print("New tree: %s" % new_tree)
                    yield self._parse(tokens, new_tree, new_frontier)
            else:
                print("Terminal, let's see if match")
                for new_tree, new_frontier in self._match(tokens, tree,
                                                          frontier):
                    yield (new_tree, new_frontier)

    def _match(self, tokens, tree, frontier):
        """ Match """
        if len(tokens) > 0 and tree[frontier[0]] == tokens[0]:
            print("Match: %s with: %s" % (tree[frontier[0]], tokens[0]))
            newtree = tree.copy()
            newtree[frontier[0]] = tokens[0]
            for new_tree, new_frontier in self._parse(tokens[1:], newtree,
                                                      frontier[1:]):
                yield (new_tree, new_frontier)
        # if len(tokens) > 0 and tree[frontier[0]] == tokens[0]:
        #     # terminal matches, let's continue parsing
        #     print("Match: %s with: %s" % (tree[frontier[0]], tokens[0]))
        #     for new_tree, new_frontier in self._parse(tokens[1:], tree,
        #                                               frontier[1:]):
        #         yield (new_tree, new_frontier)


    def _expand_tree(self, tree, frontier):
        """ expand a tree following this ``parser.grammar`` rules
            returns all possible trees by expanding the first element of
            frontier
        """
        trees = []
        frontiers = []
        if len(frontier) > 0:
            node = tree[frontier[0]]
        else:
            node = tree
        if isinstance(node, Tree):
            # Expand if node is a tree
            for production in self.grammar().productions(lhs=node.node()):
                # todo: should be a recursive call (transform method)
                new_tree, new_frontier = self.expand_tree(tree, frontier,
                                                          production)
                trees.append(new_tree)
                frontiers.append(new_frontier)
        else:
            # node can't be expanded (maybe it's a terminal)
            trees.append(tree)
            frontiers = [frontier[1:]]
        return (trees, frontiers)

    def expand_tree(self, tree, frontier, production):
        """ Expand a tree from first element of a frontier given a production

            Args:
                tree: the ``tree`` to be expanded
                frontier: the ``list`` of nodes candidates for expansion
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
        if frontier[0] == ():
            new_tree = subtree
            new_frontier = [(i, ) for i in range(len(production.rhs()))]
        else:
            new_tree = tree.copy()
            new_tree[frontier[0]] = tree_from_production(production)
            new_frontier = [frontier[0] + (i, ) for i in
                            range(len(production.rhs()))]
            new_frontier = new_frontier + frontier[1:]
        return new_tree, new_frontier
