# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search base class

from sys import argv, stderr
from wtplib.searchbase import SearchBase
from wtplib.whitehousesearch import WhiteHouseSearch
from wtplib.rankedresults import rank, inject, new_query

class WTPSearch(SearchBase):
    threshold = 10

    def search(self, query, rpp, write = True):
        '''Function to call xgoogle library and rank results'''
        self.rpp = rpp
        self.__get_results(query)
        self.__print_results() if write else None

    # Python psuedo-private methods
    def __google_search(self, query):
        '''Search google'''
        return super(WTPSearch, self).search(query, self.rpp)

    def __whitehouse_search(self, query):
        '''Search the White House site'''
        return WhiteHouseSearch(query).get_results()

    def __requires_manipulation(self, results):
        '''Returns true if the result set need additional manipulation'''
        average_weight = sum([res.weight for res in results]) / len(results)
        return average_weight < self.__class__.threshold

    def __get_results(self, query):
        '''Retrieve and rank results using our algorithm'''
        google = rank(self.__google_search(query))
        whitehouse = rank(self.__whitehouse_search(query), 2)
        results = inject(google, whitehouse)

        # Inject new query term if needed
        if self.__requires_manipulation(results):
            query = new_query(query)
            google2 = rank(self.__google_search(query), injected=True)
            results_size = len(results)
            results = inject(results, google2, results_size / 2, int(results_size * .1))

        self.results = results

    def __print_results(self):
        '''Function which prints out each result'''
        print '\n'.join([str(res) for res in self.results[:self.rpp]])

if __name__ == '__main__':
    '''Main function'''
    if len(argv) < 2:
        stderr.write('Usage: %s <query> [# results per page]\n' % argv[0])
        exit()
    rpp = int(argv[2]) if len(argv) > 2 else 25
    WTPSearch().search(argv[1], rpp)
