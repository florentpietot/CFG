# -*- coding: utf-8 -*-
#
# Author: Florent Piétot <florent.pietot@gmail.com>

""" Basic data classes for representing a basic grammar using trees.
    The leaves of a tree are words, and non-leaves nodes are defined as
    NonTerminals.
    We uses productions to define what tree structures are allowed in the
    grammar.
"""

import re

class NonTerminal(object):
    pass

class Production(object):

    def __init__(self, lhs, rhs):
        self._lhs = lhs
        self._rhs = rhs
        self._hash = hash((self._lhs, self._rhs))

    def lhs(self):
        """ Return the left hand side of this ```production```

        Returns:
            sequence
        """
        return self._lhs

    def rhs(self):
        """ Return the right hand side of this ```production```

        Returns:
            sequence
        """
        return self._rhs

    def __eq__(self, other):
        """
        Return True if this ``Production`` is equal to ``other``.
        """
        return (type(self) == type(other) and
                self._lhs == other._lhs and
                self._rhs == other._rhs)

    def __ne__(self, other):
        """ Return True if this ``Production``is not equal to ``other``
        """
        return not self == other


    @classmethod
    def _parse_production(cls, line):
        """ Parse a grammar rule, given as a string
            and returns a list of production
        """
        # TODO:
        pos = 0
        lhs = _STANDARD_NONTERM_RE.match(line)
        rhses = []
        while pos < len(line):
            pos += 1
            rhses += "N"
        return [Production(lhs, rhs) for rhs in rhses]

class Grammar(object):

    def __init__(self, productions=None):
        self._productions = productions

    def productions(self):
        """ Returns the productions for this grammar
        """
        return self._productions

    @classmethod
    def parse_grammar(cls, input):
        """ Read a grammar given as a string
        Args:
            input as a string
        Returns:
            list of `productions`
        Raises:
            TypeError if input is not a string
        """
        assert isinstance(input, str)
        lines = input.split('\n')
        productions = []
        for linenum, line in enumerate(lines):
            line = line.strip()
            if line.startswith("#") or line=="": continue
            try:
                productions += Production._parse_production(line)
            except ValueError:
                raise ValueError("Parse error on line %s: %s" % (linenum,
                                                                 line))

            test = line[1:].split(None, 1)
            print(test)
            productions.append(line)
        return productions

###############
### Helpers ###
###############

_STANDARD_NONTERM_RE = re.compile('( [\w/][\w/^<>-]* ) \s*', re.VERBOSE)
_ARROW_RE = re.compile("->", re.VERBOSE)

# def standard_nonterm_parser(string, pos):
#     m = _STANDARD_NONTERM_RE.match(string, pos)
#     if not m: raise ValueError('Expected a nonterminal, found: '
#                                + string[pos:])
#     return (Nonterminal(m.group(1)), m.end())
