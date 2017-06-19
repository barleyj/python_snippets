class MyList(object):
    """
    This is a list
    """

    my_list = []

    def size(self):
        return len(self.my_list)

    def add(self, item):
        """
        Arguments:
        - `self`:
        - `item`: Item to add to list
        """
        self.my_list.append(item)

    def get(self, item):
        """
        Arguments:
        - `self`:
        - `item`:
        """
        return item if item in self.my_list else None

    def delete(self, item):
        self.my_list.remove(item)
