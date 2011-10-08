# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search keyword list class

import re
from string import maketrans, punctuation
from collections import defaultdict
from Constants import keywords

class KeywordList:
    def __init__(self, string):
        '''Parse initial string'''
        self.words = self.__parse(string)

    # Python psuedo-private methods
    def __parse(self, string):
        '''Given a string, lowercase it, strip punctuation, and
        parse it into a dictionary mapping each keyword
        to a list of its locations in the string'''
        string = string.lower().translate(maketrans('',''), punctuation)
        words = defaultdict(list)
        for keyword in keywords():
            match = re.search(keyword, string)
            words[keyword].append(match.start()) if match else None
        return words

    # Built-ins extension
    def __str__(self):
        '''For use with str() function'''
        string = lambda x, y: '%s:\n  locations: %s\n  count: %d\n' % (x, y, len(y))
        return '\n'.join([string(k, v) for k, v in self.words.items()])
