# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

from nlp.grammar import Production, Grammar

if __name__ == "__main__":
    # nouns = ["fall", "spring", "leaves", "dog", "cat"]
    # verbs = ["spring", "leaves", "fall", "left"]
    # determiners = ["the"]
    # adjectives = ["fall", "spring", "purple", "left"]

    grammar_as_string = """
        S -> NP VP | S & S
        NP -> N | D N | Adj N | D Adj N
        VP -> V NP | V | V NP NP
        N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
        V -> 'spring' | 'leaves' | 'fall' | 'left'
        D -> 'the'
        Adj -> 'fall' | 'spring' | 'purple' | 'left
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
    # print("\n".join(parsed_grammar))
    production = "        NP -> N | D N | Adj N | D Adj N     "
    parsed_prod = Production._parse_production(production)
    print(len(parsed_prod))
