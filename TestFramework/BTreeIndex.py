__author__ = 'jesse'

import hashlib

from Index import Index

"""
Questions:
How exactly will the index be built: do we store the location of the sequence in the table and have the name be the lookup?
Or do we store the name with the sequence linked?
"""


class TreeNode:
    def __init__(self):
        pass


class BTreeIndex(Index):
    def __init__(self, disk):
        """
        Initialize the btree and set up the buckets
        """
        pass


    def put(self, key, datum):
        # Find the correct block and page to place this datum in to
        # We are going to assume that the keys are equally distributed
        # for now

        pass


    def hash_function(self, key):
        # Hash function now uses the MD5 sum of the key
        return int(hashlib.md5(str(key)).hexdigest(), 16) % self.nbuckets

    def get(self, key):
        """
         The get function retrieves the page(s) associated with the requested key
        """
        pass

    def find(self, datum):
        """
        Function for finding a specific datum in the index
        """
        # TODO Implement
        pass

    def rebalance(self):
        pass

    def bulk_load(self):
        pass