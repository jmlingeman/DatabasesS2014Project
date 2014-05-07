__author__ = 'jesse'

import hashlib

from Index import Index
from Utils import calc_stats


class Bucket:
    def __init__(self, number, disk):
        self.number = number
        self.keys = []
        self.pages = []
        self.key_access_count = []
        self.disk = disk
        self.key_to_page = {}

    def find_key(self, key):
        for i, k in enumerate(self.keys):
            self.key_access_count[i] += 1
            if key == k:
                return self.pages[i].get()

    def find_key_and_write(self, key):
        for i, k in enumerate(self.keys):
            self.key_access_count[i] += 1
            if key == k:
                self.pages[i].writes += 1
                return self.pages[i].get()

    def put(self, key, datum):
        if key not in self.keys:
            self.keys.append(key)
            self.key_access_count.append(0)
            page = self.disk.request_page()
            self.key_to_page[key] = page
            self.pages.append(page)

        # print key, datum, self.keys, self.key_to_page

        self.key_to_page[key].append(datum)
        # TODO Try to add this datum to a page that is in this key


class HashIndex(Index):
    def __init__(self, disk, nbuckets):
        """
        Initialize the hash index and set up the buckets
        """
        self.disk = disk
        self.nbuckets = nbuckets
        self.buckets = {}
        for i in range(self.nbuckets):
            self.buckets[i] = Bucket(i, disk)


    def insert(self, key, datum):
        # Find the correct block and page to place this datum in to
        # We are going to assume that the keys are equally distributed
        # for now

        bucket_number = self.hash_function(key)
        bucket = self.buckets[bucket_number]
        bucket.put(key, datum)


    def hash_function(self, key):
        # Hash function now uses the MD5 sum of the key
        return int(hashlib.md5(str(key)).hexdigest(), 16) % self.nbuckets

    def get(self, key):
        """
         The get function retrieves the page(s) associated with the requested key
        """
        bucket_number = self.hash_function(key)
        bucket = self.buckets[bucket_number]
        res = bucket.find_key(key)
        if res == None:
            return []
        else:
            return res

    def get_and_write(self, key):
        """
         The get function retrieves the page(s) associated with the requested key
        """
        bucket_number = self.hash_function(key)
        bucket = self.buckets[bucket_number]
        res = bucket.find_key_and_write(key)
        if res == None:
            return []
        else:
            return res

    def find(self, datum):
        """
        Function for finding a specific datum in the index
        """
        # TODO Implement
        pass

    def get_statistics(self):

        reads = []
        writes = []

        for block in self.disk.blocks:
            for page in block.pages:
                reads.append(page.reads)
                writes.append(page.writes)

        return calc_stats(reads, writes)