# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search constants storage

import re
from os import path

file_path = path.join(path.dirname(__file__), 'data')

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
def signaldata():
    '''Memoize the contents of the signaldata file'''
    regex = re.compile('^(?P<type>\w+) (?P<weight>[\d.]+)')
    with open(path.join(file_path, 'signaldata.txt')) as f:
        matches = [regex.match(line).groupdict() for line in f]
        return {x['type'] : float(x['weight']) for x in matches}

@memoize
def keywords():
    '''Memoize the contents of the keywords file.'''
    regex = re.compile('^(?P<word>[\w ]+) (?P<weight>\d+)')
    with open(path.join(file_path, 'keywords.txt')) as f:
        matches = [regex.match(line).groupdict() for line in f]
        return {x['word'] : int(x['weight']) for x in matches}

@memoize
def taglines():
    '''Memoize the contents of the taglines file.'''
    with open(path.join(file_path, 'taglines.txt')) as f:
        return list(f)
