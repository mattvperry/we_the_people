# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search base class

from sys import argv, stderr
from wtplib.searchbase import SearchBase
from wtplib.rankedresults import rank

class WTPSearch(SearchBase):
    def search(self, query, rpp, write = True):
        '''Function to call xgoogle library and rank results'''
        self.results = rank(super(WTPSearch, self).search(query, rpp))
        self.print_results() if write else None
        return self.results

    def print_results(self):
        '''Function which prints out each result'''
        print '\n'.join([str(res) for res in self.results])

if __name__ == '__main__':
    '''Main function'''
    if len(argv) < 2:
        stderr.write('Usage: %s <query> [# results per page]\n' % argv[0])
        exit()
    rpp = int(argv[2]) if len(argv) > 2 else 25
    WTPSearch().search(argv[1], rpp)
