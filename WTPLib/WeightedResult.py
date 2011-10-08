# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search weighted result class

from KeywordList import KeywordList

class WeightedResult:
    def __init__(self, result):
        '''Initialize member variables'''
        self.title = result.title.encode('utf-8')
        self.desc = result.desc.encode('utf-8')
        self.url = result.url.encode('utf-8')
        self.weight = 0
        self.keywords = self.collect_keywords('title', 'desc')

    def __str__(self):
        '''For use with str() function'''
        return ('%s\n%s\n%s\n' % (self.title, self.desc, self.url))

    def collect_keywords(self, *args):
        '''Collect the keywords from each portion of the result
        into a dictionary of KeywordList classes'''
        keyword_analysis = lambda x: KeywordList(getattr(self, x))
        return {meth : keyword_analysis(meth) for meth in args}
