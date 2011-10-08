# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search results ranker

from WeightedResult import WeightedResult

def rank(results):
    '''Given a list of results, rank them using our algorithm'''
    results = [WeightedResult(res) for res in results]
    return results
