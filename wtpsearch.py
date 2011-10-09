# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search base class

from sys import argv, stderr
from wtplib.searchbase import SearchBase
from wtplib.whitehousesearch import WhiteHouseSearch
from wtplib.rankedresults import rank, inject

class WTPSearch(SearchBase):
    def search(self, query, rpp, write = True):
        '''Function to call xgoogle library and rank results'''
        self.query = query
        self.rpp = rpp
        self.__get_results(query, rpp)
        self.__print_results() if write else None
        return self.results

    # Python psuedo-private methods
    def __google_search(self):
        return super(WTPSearch, self).search(self.query, self.rpp)

    def __whitehouse_search(self):
        return WhiteHouseSearch(self.query).get_results()

    def __get_results(self, query, rpp):
        '''Retrieve and rank results using our algorithm'''
        google = rank(self.__google_search())
        whitehouse = rank(self.__whitehouse_search())
        self.results = inject(google, whitehouse)

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
