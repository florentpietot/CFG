# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

from cfg.grammar import Grammar
from cfg.parse import TopDownParser
from cfg.tokenize import tokenize

if __name__ == "__main__":

    grammar_as_string = """
        S0 -> S | S C S
        S -> NP VP
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

    grammar = Grammar.parse_grammar(grammar_as_string)
    parser = TopDownParser(grammar)
    tokens = tokenize(sentences[4])
    for sentence in sentences:
        tokens = tokenize(sentence)
        parse = parser.parse(tokens)
        results = [p for p in parse]
        print("==========================")
        print(sentence)
        print("--------------------------")
        for index, parse in enumerate(results):
            print("Parse #%d:\n%s" % (index, parse))
        print("--------------------------")
        print("Count: %d" % len(results))
