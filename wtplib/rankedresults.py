# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search ranking classes

import re
from string import maketrans, punctuation
from collections import defaultdict
from constants import keywords
from signals import SignalVector

def inject(primary, secondary, p_num=10, s_num=3):
    '''Inject a secondary list into the primary list
    Append the first s_num secondary items to the first p_num
    primary items, sort and reappend to the entire primary list'''
    top_ten = primary[:p_num] + secondary[:s_num]
    return sorted(top_ten, reverse=True) + primary[p_num:]

def rank(results):
    '''Turn each result into a weighted result and then sort'''
    return sorted([WeightedResult(res) for res in results], reverse=True)

def new_query(query):
    '''Given a query, return a new query which can be used for
    further manipulation of the initial search results'''
    return query + ' petition'

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
        '''For use with < operator'''
        return self.weight < other.weight

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
