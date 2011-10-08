# Chalupa Loveseats
# Web Science - Fall 2011
# We The People search weighted result class

class WeightedResult:
    def __init__(self, result):
        self.title = result.title.encode('utf-8')
        self.desc = result.desc.encode('utf-8')
        self.url = result.url.encode('utf-8')
        self.weight = 0

    def __str__(self):
        return ('%s\n%s\n%s\n' % (self.title, self.desc, self.url))
