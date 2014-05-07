__author__ = 'jesse'

import matplotlib.pyplot as plt

from CreateIndexes import *


def build_index_analysis():
    n_blocks = 1
    n_blocksize = 100
    page_size = 100
    n_buckets = 100
    order = 150

    sample_factor = 500

    data, names, id_to_num, num_to_id, pid_to_place, place_to_pid = read_trajectory_data("../../postFSM.txt")

    hash_index_stats = []
    disk = Disk(n_blocks, n_blocksize, page_size)
    hash_index = HashIndex(disk, n_buckets)
    print "Creating id => trajectory hash"
    for i, d in enumerate(data):
        hash_index.insert(d[0], d[1])
        if i % sample_factor == 0:
            hash_index_stats.append(hash_index.get_statistics())

    print "Creating location => id hash"
    hash_loc_to_id_stats = []
    disk_loc_to_id = Disk(n_blocks, n_blocksize, page_size)
    hash_loc_to_id = HashIndex(disk_loc_to_id, n_buckets)
    for i, d in enumerate(data, i):
        for t in d[1]:
            r = hash_loc_to_id.get(t)
            if len(r) == 0:
                hash_loc_to_id.insert(t, [d[0]])
            else:
                if d[0] not in r:
                    hash_loc_to_id.get_and_write(t).append(d[0])
        if i % sample_factor == 0:
            hash_loc_to_id_stats.append(hash_loc_to_id.get_statistics())

    print "Creating location => id hash with idx"
    hash_loc_to_id_stats = []
    disk_loc_to_id_idx = Disk(n_blocks, n_blocksize, page_size)
    hash_loc_to_id_idx = HashIndex(disk_loc_to_id_idx, n_buckets)
    for j, d in enumerate(data):
        for i, t in enumerate(d[1]):
            r = hash_loc_to_id_idx.get(t)
            if len(r) == 0:
                hash_loc_to_id_idx.insert(t, [(d[0], i)])
            else:
                hash_loc_to_id_idx.get_and_write(t).append((d[0], i))
        if j % sample_factor == 0:
            hash_loc_to_id_stats.append(hash_loc_to_id_idx.get_statistics())

    print len(hash_index_stats)
    print hash_index_stats
    print plot_stats_array(hash_loc_to_id_stats, "", 500)


def plot_stats_array(stats, name, sample_factor):
    combined_stats = {}
    for statname in stats[0].keys():
        s = []
        for stat in stats:
            s.append(stat[statname])
        plt.plot(s)
        plt.show()


if __name__ == "__main__":
    build_index_analysis()


