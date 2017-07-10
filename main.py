# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

from nlp.grammar import Production, Grammar
from nlp.tree import Tree

if __name__ == "__main__":
    # nouns = ["fall", "spring", "leaves", "dog", "cat"]
    # verbs = ["spring", "leaves", "fall", "left"]
    # determiners = ["the"]
    # adjectives = ["fall", "spring", "purple", "left"]

    grammar_as_string = """
        S -> NP VP | S S
        NP -> N | D N | Adj N | D Adj N
        VP -> V NP | V | V NP NP
        N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
        V -> 'spring' | 'leaves' | 'fall' | 'left'
        D -> 'the'
        Adj -> 'fall' | 'spring' | 'purple' | 'left'
    """

    sentences = [
        "Fall leaves fall.",
        "Fall leaves fall and spring leaves spring.",
        "The fall leaves left.",
        "The purple dog left",
        "The dog and cat left"
    ]

    # grammar = Grammar()
    # parsed_grammar = Grammar().parse_grammar(grammar_as_string)
    # print(parsed_grammar)

    # node = "root_node"
    # child_1 = Tree(node="child1", children=["grandchild1-1",
    #                                         "grandchild1-2",
    #                                         "grandchild1-3"])
    # child_2 = Tree(node="child2")
    # child_3 = Tree(node="child3", children=["grandchild3-1",
    #                                        "grandchild3-2",
    #                                        "grandchild3-3"])
    # children = [child_1, child_2, child_3]
    # tree = Tree(node=node, children=children)
    # print(tree.leaves())

    lines = []
    lines.append("NP -> N | D N | Adj N | D Adj N")
    lines.append("Adj -> 'fall' | 'spring' | 'purple' | 'left'")
    for line in lines:
        print(Production._parse_production(line))
