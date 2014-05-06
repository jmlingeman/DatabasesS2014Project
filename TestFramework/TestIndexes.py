from TestFramework.Disk import Disk
from TestFramework.HashIndex import HashIndex
from DataParser import read_trajectory_data
from BTree import BPlusTree

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

hash_index.get(2)

# Print its results
hash_index.print_status()

# Teat reading in the trajectory data
data, names, id_to_num, num_to_id, pid_to_place, place_to_pid = read_trajectory_data("../../postFSM.txt")

# Create a simple BTree of id => trajectory
# Start with an order 50
btree = BPlusTree(150)
for d in data:
    btree.insert(d[0], d[1])

# print btree.get(1)

