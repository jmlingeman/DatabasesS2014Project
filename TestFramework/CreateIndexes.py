import time

from Disk import Disk
from HashIndex import HashIndex
from DataParser import read_trajectory_data
from BTreeIndex import BPlusTree


__author__ = 'jesse'


def create_btree_indexes():
    # Create a new hash index
    n_blocks = 5
    n_blocksize = 10
    page_size = 5
    n_buckets = 5
    order = 150

    disk = Disk(n_blocks, n_blocksize, page_size)
    hash_index = HashIndex(disk, n_buckets)

    # Add some data to it
    hash_index.put(1, "key")
    hash_index.put(2, "key")
    hash_index.put(3, "key")
    hash_index.put(4, "key")

    hash_index.get(2)

    # Print its results
    # hash_index.print_status()

    # Teat reading in the trajectory data
    data, names, id_to_num, num_to_id, pid_to_place, place_to_pid = read_trajectory_data("../../postFSM.txt")

    # print create_ngrams(data[1][1], 2)

    # Create a simple BTree of id => trajectory
    # Start with an order 50
    print "Creating id => trajectory btree"
    btree = BPlusTree(150)
    for d in data:
        btree.insert(d[0], d[1])

    # Create an index of location => ids
    print "Creating location => id btree"
    stime = time.time()
    btree_loc_to_id = BPlusTree(order)
    for d in data:
        for t in d[1]:
            r = btree_loc_to_id.get(t)
            if r == None:
                btree_loc_to_id.insert(t, [d[0]])
            else:
                btree_loc_to_id.get(t).append(d[0])

    # print time.time() - stime

    # print btree_loc_to_id.get(names[0])

    print "Creating location => id + idx btree"
    stime = time.time()
    btree_loc_to_id_idx = BPlusTree(order)
    for d in data:
        for i, t in enumerate(d[1]):
            r = btree_loc_to_id_idx.get(t)
            if r == None:
                btree_loc_to_id_idx.insert(t, [(d[0], i)])
            else:
                btree_loc_to_id_idx.get(t).append((d[0], i))

    # print time.time() - stime
    # print btree_loc_to_id_idx.get(names[0])

    # # Same tree but with ngrams
    # # Create an index of location => ids
    # print "Creating location => id ngram2 btree"
    # stime = time.time()
    # btree_loc_to_id_2gram = BPlusTree(order)
    # for d in data:
    #     for i, t in enumerate(create_ngrams(d[1], 2)):
    #         r = btree_loc_to_id_2gram.get(t)
    #         if r == None:
    #             btree_loc_to_id_2gram.insert(t, [d[0]])
    #         else:
    #             btree_loc_to_id_2gram.get(t).append(d[0])
    #
    # print time.time() - stime
    # print btree_loc_to_id_2gram.get([names[0], names[0]])
    #
    # print "Creating location => id idx ngram2 btree"
    # stime = time.time()
    # btree_loc_to_id_2gram_idx = BPlusTree(order)
    # for d in data:
    #     for i, t in enumerate(create_ngrams(d[1], 2)):
    #         r = btree_loc_to_id_2gram_idx.get(t)
    #         if r == None:
    #             btree_loc_to_id_2gram_idx.insert(t, [(d[0], i)])
    #         else:
    #             btree_loc_to_id_2gram_idx.get(t).append((d[0], i))
    #
    # print time.time() - stime
    # print btree_loc_to_id_2gram_idx.get([names[0], names[0]])
    # print len(list(btree_loc_to_id_2gram_idx))

    return btree, btree_loc_to_id, btree_loc_to_id_idx



    # print btree.get(1)


