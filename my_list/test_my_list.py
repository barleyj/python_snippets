from my_list import MyList
from hypothesis.strategies import integers, just
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule
import unittest


class MyListTests(RuleBasedStateMachine):
    my_list = Bundle('MyList')
    item = Bundle('Item')
    incremented = Bundle('Count')
    size = Bundle('Size')
    added = Bundle('Added')
    addedv = Bundle('Addedv')
    deleted = Bundle('Deleted')

    @rule(target=my_list)
    def init(self):
        return MyList()

#    @rule(target=size, ls=my_list)
#    def init_size(self, ls):
#        return -1

    @rule(target=item, x=just('blah'), ls=my_list)
    def create_item(self, x, ls):
        ls.add(x)
        return x

    @rule(x=item, ls=my_list)
    def check_size(self, ls, x):
#        print 'Check_size: ' + str(size)
#        assert ls.size() == size + 1
        assert ls.get(x) == x

    ## @rule(target=added, ls=my_list, x=item)
    ## def add(self, ls, x):
    ##     print 'Adding: ' + str(x)
    ##     ls.add(x)
    ##     return x

    ## @rule(ls=my_list, x=added)
    ## def check_inserted(self, ls, x):
    ##     print 'check_inserted: ' + str(x)
    ##     assert ls.get(x) == 0

    ## @rule(target=deleted, ls=my_list, x=added)
    ## def delete(self, ls, x):
    ##     print x
    ##     ls.delete(x)
        ## return x

    ## @rule(ls=my_list, x=added)
    ## def check_deleted(self, ls, x):
    ##     assert ls.get(x) == None

TestSet = MyListTests.TestCase

if __name__ == '__main__':
    unittest.main()
