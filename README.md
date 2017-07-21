# Basic Context-Free Grammar

A few months ago, I followed Udacity's [Intro to Artificial Intelligence](https://www.udacity.com/course/intro-to-artificial-intelligence--cs271) by Peter Norvig and Sebastian Thrun.

I realized I had forgotten to finish a couple of exercises in the final assignment. One of those exercises wasn't difficult to solve "manually", but seemed like an interesting exercise to solve programmatically: good low-level introduction to NLP and python's unittest module.

## Exercise
Here is the exercise
![Grammar exercice from Udacity's intro to Artificial Intelligence](/screenshots/grammar-exercice.png?raw=true "Grammar exercice from Udacity's intro to artificial intelligence")

## How to use
Create a TopDownParser object given a grammar. This grammar can be initialized
through Grammar.parse_grammar() which will parse a grammar given in a string
form.

Example of a grammar as a string form:
    
    grammar_as_string = """
    S -> NP VP,\n
    NP -> N | D N,
    VP -> V | V NP,
    N -> 'fall' | 'leaves' | 'spring',
    D -> 'the'
    """

The left-hand side of the first encountered production will be used 
as the starting point for the grammar.

Let's init a grammar object with this grammar as a string:
    
    grammar = Grammar.parse_grammar(grammar_as_string)

Then create a TopDownParser from this grammar:
    
    parser = TopDownParser(grammar)

## Limitations
This code won't handle grammars in Non-Chomsky form, in particular it won't
handle grammar with productions containing the start symbol in the right-hand
side of any of their production.

Given the grammar given in Udacity's exercise wasn't of this form, in
particular there was a production of the form S -> S and S (given S is the
start symbol for this grammar), I actually manually edited this grammar by
introducing a new "S0" start symbol and rewrite productions accordingly.
See "Improvements" about this.

## Improvements
### Structure
I tried to keep the models simple, only building models that were required to
make things work properly. Because of this, I skipped implementing some of the
things that would normarly be implemented by a production ready module. For
example, I didn't implement any way of discriminating between Terminals and
Non-Terminals. I ended up doing some quick fix by checking if there was a ' at
the end of the string for discriminating between them.

### Handle Non-Chomsky form
The code currently won't handle Non-Chomsky. It should be possible to rewrite
any Non-Chomsky form grammar into a Chomsky form, this could be implemented in
future developments.

### Tests
That was my first approach with python's unittest module. I feel like there is
a lot of room for improvement here, maybe using a module like ``nose`` could help but I have a hunch there is already much more that could be done with proper usage of ``unittest``, like using decorators, subclassing, etc.. Any feedbacks are welcome.

In particular, the functions used by the TopDownParser (``_parse``, ``_expand``, ``_match``)
are difficult to test in isolation given parse call both ``_expand`` and ``_match``, and
``_expand``/``_match`` both are calling ``_parse``.
What I'm interested in testing for each of those, is the next step in the
recursion. E.g. for expand, what will be the next tree candidates for expansion
that will then be sent for parsing.

## Feedback
That was quite a good introduction to low-level NLP concepts for me. NLP is a
pretty dense topic, with all kind of specific vocabulary, etc...

## Contact
You can contact me at florent.pietot[at]gmail.com
