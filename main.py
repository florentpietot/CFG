# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

from nlp.grammar import Production, Grammar
from nlp.tree import Tree, tree_from_production

if __name__ == "__main__":

    grammar_as_string = """
        S -> NP VP | S C S
        NP -> N | D N | Adj N | D Adj N
        VP -> V NP | V | V NP NP
        N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
        V -> 'spring' | 'leaves' | 'fall' | 'left'
        D -> 'the'
        C -> 'and'
        Adj -> 'fall' | 'spring' | 'purple' | 'left'
    """

    sentences = [
        "Fall leaves fall.",
        "Fall leaves fall and spring leaves spring.",
        "The fall leaves left.",
        "The purple dog left",
        "The dog and cat left"
    ]

