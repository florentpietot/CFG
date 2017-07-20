
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Tests for parse.py module
"""

import unittest
from nlp.tree import Tree, tree_from_production
from nlp.parse import TopDownParser
from nlp.grammar import Grammar, Production

class TestTopDownParserInit(unittest.TestCase):
    """ Init tests """

    def setUp(self):
        grammar_as_string = """
        NP -> N | D N
        N -> 'fall' | 'spring' | 'leaves' | 'dog' | 'cat'
        D -> 'the'
        """
        self.grammar = Grammar.parse_grammar(grammar_as_string)
        self.parser = TopDownParser(self.grammar)

    def test_returns_grammar(self):
        """ Check it returns the ``grammar`` param properly """
        res = self.parser.grammar()
        self.assertEqual(res, self.parser.grammar(),
                         "It should return the grammar")


class TestParse(unittest.TestCase):

    def setUp(self):
        grammar_as_string = """
            S -> NP VP
            NP -> N | D N | Adj N | D Adj N
            VP -> V NP | V |V NP NP
            N -> 'fall' | 'spring' | 'leaves'
            V -> 'spring' | 'leaves' | 'fall'
            D -> 'the'
            Adj -> 'fall' | 'spring' | 'purple'
        """
        grammar = Grammar.parse_grammar(grammar_as_string)
        self.parser = TopDownParser(grammar)

    def test_non_parsable(self):
        tokens = ["hello", "world"]
        with self.assertRaises(StopIteration):
            next(self.parser.parse(tokens))

    def test_one_parse(self):
        print("============================")
        print("Test one parse")
        tokens = ["fall", "leaves"]
        res = Tree("S", [Tree("NP", [Tree("N", ["'fall'"])]),
                         Tree("VP", [Tree("V", ["'leaves'"])])])
        parse = self.parser.parse(tokens)
        self.assertEqual(res, next(parse)[0])
        print("============================")

    def test_multiple_parse(self):
        pass

class TestPrivateParse(unittest.TestCase):

    def setUp(self):
        grammar_as_string = """
            S -> NP VP
            NP -> N | D N | Adj N | D Adj N
            VP -> V NP | V |V NP NP
            N -> 'fall' | 'spring' | 'leaves'
            V -> 'spring' | 'leaves' | 'fall'
            D -> 'the'
            Adj -> 'fall' | 'spring' | 'purple'
        """
        grammar = Grammar.parse_grammar(grammar_as_string)
        self.parser = TopDownParser(grammar)
        self.tree = Tree("S", [])
        self.tokens = ["'fall'", "'leaves'", "'fall'"]
        self.frontier = [()]

    def test_parse_with_final_match(self):
        self.tree = Tree("N", ["'fall'"])
        self.tokens = ["fall"]
        self.frontier = [(0, )]
        res = self.tree
        parse = self.parser._parse(self.tokens, self.tree, self.frontier)
        new_tree, new_frontier = next(parse)
        self.assertListEqual(res, new_tree)

class TestMatch(unittest.TestCase):
    """ Tests for TopDownParser()._match(tokens, tree, frontier)
    """

    def setUp(self):
        grammar_as_string = """
            NP -> N | D N
            N -> 'fall' | 'spring' | 'leaves'
            D -> 'the'
        """
        grammar = Grammar.parse_grammar(grammar_as_string)
        self.parser = TopDownParser(grammar)
        self.tree = Tree("NP", [Tree("D", []), Tree("N", [])])
        self.frontier = [(0, ), (1, )]
        self.tokens = ["'the'", "'fall'"]

    def test_tokens_is_empty(self):
        self.tokens = []
        with self.assertRaises(ValueError):
            next(self.parser._match(self.tokens, self.tree, self.frontier))

    def test_frontier_is_empty(self):
        self.frontier = []
        with self.assertRaises(ValueError):
            next(self.parser._match(self.tokens, self.tree, self.frontier))

    def test_frontier_is_not_a_match(self):
        """ Should yield nothing """
        self.tree[self.frontier[0]].append("'a'")
        self.frontier = [(0, 0), (1, )]
        with self.assertRaises(StopIteration):
            next(self.parser._match(self.tokens, self.tree, self.frontier))


class TestExpand(unittest.TestCase):
    """ Test parse._expand(tree, frontier)
        Hence, multiple productions candidates are possible
        That means the function can yield more than one (tree, frontier)
    """

    def setUp(self):
        grammar_as_string = """
            NP -> N | D N
            N -> 'fall' | 'srpring' | 'leaves'
            D -> 'the'
        """
        grammar = Grammar.parse_grammar(grammar_as_string)
        self.parser = TopDownParser(grammar)
        self.tokens = ["hello", "world"]

    def test_expand_with_empty_frontier(self):
        """ Assert ValueError is raised if frontier is empty """
        tree = Tree("S", [])
        frontier = []
        with self.assertRaises(ValueError):
            next(self.parser._expand(self.tokens, tree, frontier))

    # #TODO: Can't test this because of recursions
    # def test_expand_into_a_single_tree(self):
    #     """ Single expand """
    #     tree = Tree("NP", [Tree("D", []), Tree("N", [])])
    #     frontier = [(0, ), (1, )]
    #     res_tree = Tree("NP", [Tree("D", ["'the'"]), Tree("N", [])])
    #     res_frontier = [(0, 0), (1, )]
    #     res = (res_tree, res_frontier)
    #     self.tokens = ["the", "fall"]
    #     parse = self.parser._expand(self.tokens, tree, frontier)
    #     self.assertTupleEqual(res, next(parse))

    def test_expand_non_expandable(self):
        """ It should return a StopIteration error """
        tree = Tree("NP", [Tree("D", ["'the'"]), Tree("N", [])])
        frontier = [(0, 0), (1, )]
        parse = self.parser._expand(self.tokens, tree, frontier)
        with self.assertRaises(StopIteration):
            next(self.parser._expand(self.tokens, tree, frontier))


if __name__ == "__main__":
    unittest.main()
