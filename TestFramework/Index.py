__author__ = 'jesse'


class Index:
    """
    The generic class that all of the indexes will be instantiated from
    """

    def __init__(self, disk):
        self.disk = disk

    def build_disk(self, dataset):
        for i, data in enumerate(dataset):
            self.disk.put(data)


    def put(self, key, data):
        pass

    def get(self, key):
        pass
