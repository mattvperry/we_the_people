# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search signals

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
    # TODO: Apply some kind of decay function to the number of times the keyword appears
    word_weight = lambda x, y: keywords()[x] * len(word_matrix[y].words[x])
    title = sum([word_weight(x, 'title') for x in word_matrix['title'].words])
    desc = sum([word_weight(x, 'desc') for x in word_matrix['desc'].words])
    return title + desc

def location(word_matrix):
    '''Apply additional weight to keywords appearing
    in the header of the result'''
    # TODO: Apply some kind of decay function to the number of times the keyword appears
    word_weight = lambda x, y: keywords()[x] * len(word_matrix[y].words[x])
    return sum([word_weight(x, 'title') for x in word_matrix['title'].words])

def proximity(word_matrix):
    '''Apply additional weight to keywords which
    appear close to other keywords'''
    distance_sum = 0
    for section in ['title', 'desc']:
        words_hash = word_matrix[section].words
        if len(words_hash) <= 1:
            break
        for (word, locations) in words_hash.items():
            for (word2, locations2) in words_hash.items():
                if word == word2:
                    continue
                for location in locations:
                    for location2 in locations2:
                        if location > location2:
                            distance_sum += location - (location2 + len(word2))
                        elif location < location2:
                            distance_sum += location2 - (location + len(word))
        if len(words_hash) > 0:
            distance_sum //= len(words_hash)
    return distance_sum // 2
