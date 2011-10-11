# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search constants storage

import re, json
from os import path

config_file = path.join(path.dirname(__file__), 'config.json')

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
def config():
    with open(config_file) as conf:
        return json.loads(conf.read());

def signaldata():
    return config()['signaldata']

def keywords():
    return config()['keywords']

def taglines():
    return config()['taglines']
