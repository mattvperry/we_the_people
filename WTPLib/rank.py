# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search results ranker

from WeightedResult import WeightedResult

def rank(results):
    return [WeightedResult(res) for res in results]
