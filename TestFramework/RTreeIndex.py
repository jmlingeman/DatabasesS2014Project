from Index import Index

__author__ = 'jesse'


class RTreeIndex(Index):
    def __init__(self):
        """
        This index requires some sort of coordinates for each data entry.
        This doesn't really work for us, but we could generate coordinates via clustering

        For example, we can use k-means clustering on the dataset and get the position in the clustering
        relative to all of the other strings
        """
        pass

    def cluster(self, datum):
        pass

    def bulk_load(self, datum):
        pass