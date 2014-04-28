__author__ = 'jesse'

from Index import Index


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

    def put(self, key, datum):
        if key not in self.keys:
            self.keys.append(key)
            self.key_access_count.append(0)
            page = self.disk.request_page()
            self.key_to_page[key] = page
            self.pages.append(page)

        self.key_to_page[key].append(datum)


        # TODO Try to add this datum to a page that is in this key


class HashIndex(Index):
    def __init__(self, disk, nbuckets):
        self.disk = disk
        self.nbuckets = nbuckets
        self.buckets = {}
        for i in range(self.nbuckets):
            self.buckets[i] = Bucket(i, disk)


    def put(self, key, datum):
        # Find the correct block and page to place this datum in to
        # We are going to assume that the keys are equally distributed
        # for now

        bucket_number = self.hash_function(key)
        bucket = self.buckets[bucket_number]
        bucket.put(key, datum)


    def hash_function(self, key):
        # Super simple hash function
        # TODO Make this function better
        return key % self.nbuckets

