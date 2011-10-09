# Chalupa Loveseats
# Web Science - Fall 2011
# We The People Search API for whitehouse.gov

import re
from urllib2 import urlopen
from xgoogle.BeautifulSoup import BeautifulSoup

class WhiteHouseSearch:
    endpoint = 'https://wwws.whitehouse.gov/petition-tool/petitions/more/all/0/2/0/'
    regex = re.compile('<a href="">(?P<title>.*)<\\\/a>.*<span class="">(?P<sigs>[\d,]+)')

    def __init__(self, query):
        '''Initialize query term'''
        self.query = query

    def get_results(self):
        '''Query the white house and parse results'''
        html = urlopen(self.__url())
        a_tags = BeautifulSoup(html).findAll('a')
        return [self.__create_result(a) for a in a_tags[:-1:2]]

    # Python psuedo-private functions
    def __url(self):
        '''Create the query url from the endpoint and the query'''
        return self.__class__.endpoint + self.query

    # The HTML from the White House is malformed... doing my best
    # to extract relevant data.
    def __create_result(self, tag):
        '''Parse each part of the response HTML into a result object'''
        match = self.__class__.regex.search(str(tag))
        return WhiteHouseResult(match.groupdict())

# Class to coerce results from the whitehouse into results
# similar to xgoogle
class WhiteHouseResult:
    title = 'We The People - The White House'

    def __init__(self, info_dict):
        '''Initialize member variables'''
        self.title = self.__class__.title
        self.desc = info_dict['title']
        self.url = info_dict['sigs'] + ' Signatures'
