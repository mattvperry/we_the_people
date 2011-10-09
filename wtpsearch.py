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
        self.__get_results(query, rpp)
        self.__print_results() if write else None

    # Python psuedo-private methods
    def __google_search(self, query, rpp):
        '''Search google'''
        return super(WTPSearch, self).search(query, rpp)

    def __whitehouse_search(self, query):
        '''Search the White House site'''
        return WhiteHouseSearch(query).get_results()

    def __requires_manipulation(results):
        '''Returns true if the result set need additional manipulation'''
        average_weight = sum([res.weight for res in results]) / len(results)
        return average_weight < self.__class__.threshold

    def __get_results(self, query, rpp):
        '''Retrieve and rank results using our algorithm'''
        google = rank(self.__google_search(query, rpp))
        whitehouse = rank(self.__whitehouse_search(query))
        results = inject(google, whitehouse)

        # Inject new query term if needed
        if __requires_manipulation(results):
            query = new_query(query)
            google2 = rank(self.__google_search(query, rpp))
            results = inject(results, google2, 20, 10)

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
