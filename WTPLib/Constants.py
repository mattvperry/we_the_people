# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search constants storage

import re
from os import path

file_path = path.dirname(__file__)

def memoize(func):
    '''Memoize python decorator. Given a function,
    return a meta function which will save the output
    for later uses.'''
    def inner():
        if inner.cache is None:
            inner.cache = func()
        return inner.cache
    inner.cache = None
    return inner

@memoize
def keywords():
    '''Memoize the contents of the keywords file.'''
    regex = re.compile('^(?P<word>[\w ]+) (?P<weight>\d+)')
    with open(path.join(file_path, 'keywords.txt')) as f:
        matches = [regex.match(line).groupdict() for line in f]
        return {x['word'] : x['weight'] for x in matches}

@memoize
def taglines():
    '''Memoize the contents of the taglines file.'''
    with open(path.join(file_path, 'taglines.txt')) as f:
        return list(f)
