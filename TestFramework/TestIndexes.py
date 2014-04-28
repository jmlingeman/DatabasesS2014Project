from TestFramework.Disk import Disk
from TestFramework.HashIndex import HashIndex

__author__ = 'jesse'

# Create a new hash index
n_blocks = 5
n_blocksize = 10
page_size = 5
n_buckets = 5

disk = Disk(n_blocks, n_blocksize, page_size)
hash_index = HashIndex(disk, n_buckets)

# Add some data to it
hash_index.put(1, "key")
hash_index.put(2, "key")
hash_index.put(3, "key")
hash_index.put(4, "key")


# Print its results
hash_index.print_status()