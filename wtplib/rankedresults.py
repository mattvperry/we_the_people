# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search ranking classes

import re
from string import maketrans, punctuation
from collections import defaultdict
from constants import keywords
from signals import SignalVector
from whitehousesearch import WhiteHouseSearch

def rank(results):
    '''Given a list of results, rank them using our algorithm'''
    results = [WeightedResult(res) for res in results]
    results.sort(reverse=True)
    return results

class WeightedResult:
    debug = True

    def __init__(self, result):
        '''Initialize member variables'''
        self.title = result.title.encode('utf-8')
        self.desc = result.desc.encode('utf-8')
        self.url = result.url.encode('utf-8')
        self.keywords = self.__collect_keywords('title', 'desc')
        self.weight = SignalVector(self.keywords).total_weight

    # Python psuedo-private methods
    def __collect_keywords(self, *args):
        '''Collect the keywords from each portion of the result
        into a dictionary of KeywordList classes'''
        keyword_analysis = lambda x: KeywordList(getattr(self, x))
        return {meth : keyword_analysis(meth) for meth in args}

    # Built-ins extension
    def __lt__(self, other):
        return True if self.weight < other.weight else False

    def __str__(self):
        '''For use with str() function'''
        if self.__class__.debug:
            return ('Weight: %d\n%s\n%s\n%s\n' % (self.weight, self.title, self.desc, self.url))
        else:
            return ('%s\n%s\n%s\n' % (self.title, self.desc, self.url))

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
