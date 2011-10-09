# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search signal collection vector

from sys import modules
from constants import keywords, signaldata

class SignalVector:
    def __init__(self, word_matrix):
        '''Initialize weights'''
        self.weights = self.__weigh(word_matrix)
        self.total_weight = self.__apply_coefficients()

    # Python psuedo-private methods
    def __weigh(self, word_matrix):
        '''Given a matrix of words, assign a number associated
        with each type of signal'''
        get_func = lambda f: getattr(modules[__name__], f)
        return {t : get_func(t)(word_matrix) for t in signaldata()}

    def __apply_coefficients(self):
        '''Multiply and add each individual signal with the
        coefficient vector'''
        return sum([self.weights[t] * w for t, w in signaldata().items()])

def weight(word_matrix):
    '''Simple addition of weights of each keyword
    appearing in the result'''
    return 1

def location(word_matrix):
    '''Apply additional weight to keywords appearing
    in the header of the result'''
    return 1

def proximity(word_matrix):
    '''Apply additional weight to keywords which
    appear close to other keywords'''
    return 1
