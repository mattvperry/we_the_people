#S. Ardizzone
#FA2010
#ABC to interface with xgoogle library

from abc import ABCMeta, abstractmethod, abstractproperty
from xgoogle.search import GoogleSearch, SearchError

class SearchBase:
    __metaclass__ = ABCMeta

    @abstractmethod
    def search(self, query, rpp):
        gs = GoogleSearch(query)
        gs.results_per_page = rpp
        return gs.get_results()
