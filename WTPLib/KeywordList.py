# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search keyword list class

from string import maketrans, punctuation
from collections import defaultdict

class KeywordList:
    def __init__(self, string):
        '''Parse initial string'''
        self.words = self.parse(string)

    def __str__(self):
        '''For use with str() function'''
        string = lambda x, y: '%s:\n  locations: %s\n  count: %d\n' % (x, y, len(y))
        return '\n'.join([string(k, v) for k, v in self.words.items()])

    def parse(self, string):
        '''Given a string, lowercase it, strip punctuation, and
        parse it into a dictionary mapping each word
        to a list of its locations in the string'''
        string = string.lower().translate(maketrans('',''), punctuation)
        words = defaultdict(list)
        [words[word].append(i) for i, word in enumerate(string.split())]
        return words
