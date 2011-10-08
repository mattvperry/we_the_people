# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search weighted result class

from KeywordList import KeywordList
from SignalVector import SignalVector

class WeightedResult:
    debug = False

    def __init__(self, result):
        '''Initialize member variables'''
        self.title = result.title.encode('utf-8')
        self.desc = result.desc.encode('utf-8')
        self.url = result.url.encode('utf-8')
        self.keywords = self.__collect_keywords('title', 'desc')
        self.signals = SignalVector('weight', 'location', 'proximity')
        self.weight = self.signals.weight()

    # Python psuedo-private methods
    def __collect_keywords(self, *args):
        '''Collect the keywords from each portion of the result
        into a dictionary of KeywordList classes'''
        keyword_analysis = lambda x: KeywordList(getattr(self, x))
        return {meth : keyword_analysis(meth) for meth in args}

    # Built-ins extension
    def __str__(self):
        '''For use with str() function'''
        if self.__class__.debug:
            return ('Weight: %d\n%s\n%s\n%s\n' % (self.weight, self.title, self.desc, self.url))
        else:
            return ('%s\n%s\n%s\n' % (self.title, self.desc, self.url))
