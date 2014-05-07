import time

from Disk import Disk
from HashIndex import HashIndex
from DataParser import read_trajectory_data
from BTreeIndex import BPlusTree


__author__ = 'jesse'


def create_hash_indexes(debug=False):
    # Create a new hash index
    n_blocks = 1
    n_blocksize = 100
    page_size = 100
    n_buckets = 100

    data, names, id_to_num, num_to_id, pid_to_place, place_to_pid = read_trajectory_data("../../postFSM.txt")

    disk = Disk(n_blocks, n_blocksize, page_size)
    hash_index = HashIndex(disk, n_buckets)

    print "Creating id => trajectory hash"
    for d in data:
        hash_index.insert(d[0], d[1])
    print hash_index.get_statistics()

    print "Creating location => id hash"
    stime = time.time()
    disk_loc_to_id = Disk(n_blocks, n_blocksize, page_size)
    hash_loc_to_id = HashIndex(disk_loc_to_id, n_buckets)
    for d in data:
        for t in d[1]:
            r = hash_loc_to_id.get(t)
            if len(r) == 0:
                hash_loc_to_id.insert(t, [d[0]])
            else:
                if d[0] not in r:
                    hash_loc_to_id.get_and_write(t).append(d[0])
    print time.time() - stime
    print hash_loc_to_id.get_statistics()

    print "Creating location => id hash with idx"
    stime = time.time()
    disk_loc_to_id_idx = Disk(n_blocks, n_blocksize, page_size)
    hash_loc_to_id_idx = HashIndex(disk_loc_to_id_idx, n_buckets)
    for d in data:
        for i, t in enumerate(d[1]):
            r = hash_loc_to_id_idx.get(t)
            if len(r) == 0:
                hash_loc_to_id_idx.insert(t, [(d[0], i)])
            else:
                hash_loc_to_id_idx.get_and_write(t).append((d[0], i))
    print time.time() - stime

    print hash_loc_to_id_idx.get_statistics()

    return hash_index, hash_loc_to_id, hash_loc_to_id_idx


def create_btree_indexes(debug=False):
    order = 150

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

    if debug:
        print btree.get_statistics()

    # Create an index of location => ids
    print "Creating location => id btree"
    stime = time.time()
    btree_loc_to_id = BPlusTree(order)
    for d in data:
        for t in d[1]:
            r = btree_loc_to_id.get(t)
            if len(r) == 0:
                btree_loc_to_id.insert(t, [d[0]])
            else:
                if d[0] not in r:
                    r.append(d[0])

    if debug:
        print time.time() - stime
        # print "Loc names:"
        # print names[0], btree_loc_to_id.get(names[0])
        print btree_loc_to_id.get_statistics()

    print "Creating location => id + idx btree"
    # Will always have unique data points since is UUID, idx of occurrence
    stime = time.time()
    btree_loc_to_id_idx = BPlusTree(order)
    for d in data:
        for i, t in enumerate(d[1]):
            r = btree_loc_to_id_idx.get(t)
            if len(r) == 0:
                btree_loc_to_id_idx.insert(t, [(d[0], i)])
            else:
                # if (d[0], i) not in r:
                r.append((d[0], i))

    if debug:
        print time.time() - stime
        # print btree_loc_to_id_idx.get(names[0])
        print btree_loc_to_id_idx.get_statistics()

    # # Same tree but with ngrams
    # # Create an index of location => ids
    # print "Creating location => id ngram2 btree"
    # stime = time.time()
    # btree_loc_to_id_2gram = BPlusTree(order)
    # for d in data:
    #     for i, t in enumerate(create_ngrams(d[1], 2)):
    #         r = btree_loc_to_id_2gram.get(t)
    #         if len(r) == 0:
    #             btree_loc_to_id_2gram.insert(t, [d[0]])
    #         else:
    #             if (d[0], i) not in r:
    #               btree_loc_to_id_2gram.get(t).append(d[0])
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
    #         if len(r) == 0:
    #             btree_loc_to_id_2gram_idx.insert(t, [(d[0], i)])
    #         else:
    #             btree_loc_to_id_2gram_idx.get(t).append((d[0], i))
    #
    # print time.time() - stime
    # print btree_loc_to_id_2gram_idx.get([names[0], names[0]])
    # print len(list(btree_loc_to_id_2gram_idx))

    return btree, btree_loc_to_id, btree_loc_to_id_idx


if __name__ == "__main__":
    create_hash_indexes(True)
    create_btree_indexes(True)

    # print btree.get(1)


