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
    hash_loc_to_id_idx_stats = []
    disk_loc_to_id_idx = Disk(n_blocks, n_blocksize, page_size)
    hash_loc_to_id_idx = HashIndex(disk_loc_to_id_idx, n_buckets)
    for j, d in enumerate(data):
        for i, t in enumerate(d[1]):
            r = hash_loc_to_id_idx.get(t)
            if len(r) == 0:
                hash_loc_to_id_idx.insert(t, [(d[0], [i])])
            else:
                # if (d[0], i) not in r:
                found = False
                for k in r:
                    if k[0] == d[0]:
                        k[1].append(i)
                        found = True
                        break
                if not found:
                    r.append((d[0], [i]))
        if j % sample_factor == 0:
            hash_loc_to_id_idx_stats.append(hash_loc_to_id_idx.get_statistics())

    print len(hash_index_stats)
    print hash_index_stats
    # print plot_stats_array(hash_loc_to_id_stats, "", 500)


    print "Creating id => trajectory btree"
    btree = BPlusTree(150)
    btree_stats = []
    for i, d in enumerate(data):
        btree.insert(d[0], d[1])
        if i % sample_factor == 0:
            btree_stats.append(btree.get_statistics())

    print "Creating location => id btree"
    btree_loc_to_id = BPlusTree(order)
    btree_loc_to_id_stats = []

    for i, d in enumerate(data):
        for t in d[1]:
            r = btree_loc_to_id.get(t)
            if len(r) == 0:
                btree_loc_to_id.insert(t, [d[0]])
            else:
                if d[0] not in r:
                    r.append(d[0])
        if i % sample_factor == 0:
            btree_loc_to_id_stats.append(btree_loc_to_id.get_statistics())

    print "Creating location => id + idx btree"
    # Will always have unique data points since is UUID, idx of occurrence
    btree_loc_to_id_idx = BPlusTree(order)
    btree_loc_to_id_idx_stats = []
    for j, d in enumerate(data):
        for i, t in enumerate(d[1]):
            r = btree_loc_to_id_idx.get(t)
            if len(r) == 0:
                btree_loc_to_id_idx.insert(t, [(d[0], [i])])
            else:
                # if (d[0], i) not in r:
                found = False
                for k in r:
                    if k[0] == d[0]:
                        k[1].append(i)
                        found = True
                        break
                if not found:
                    r.append((d[0], [i]))
        if j % sample_factor == 0:
            btree_loc_to_id_idx_stats.append(btree_loc_to_id_idx.get_statistics())

    plot_multiple_stats([hash_index_stats, btree_stats], "ID to Trajectory Index", sample_factor)
    plot_multiple_stats([hash_loc_to_id_stats, btree_loc_to_id_stats], "Location to ID", sample_factor)
    plot_multiple_stats([hash_loc_to_id_idx_stats, btree_loc_to_id_idx_stats], "Location to ID with Index",
                        sample_factor)


def plot_multiple_stats(statlist, name, sample_factor):
    keys = statlist[0][0].keys()
    for key in keys:
        plt.clf()
        lines = []
        for index in statlist:
            s = []
            for stat in index:
                s.append(stat[key])
            # Plot and save the resulting handles for making the legend
            lines.append(plt.plot(s, lw=3)[0])

        locs, labels = plt.xticks()
        plt.xticks(locs, map(lambda x: x * sample_factor, locs))
        plt.xlabel("Data Point")
        plt.ylabel(key)
        plt.title(name)

        plt.legend(lines, ["Hash Index", "BTree Index"], loc=4)

        # plt.tight_layout()
        plt.savefig("../Graphs/" + name + "-" + key + ".pdf")
        # plt.show()


if __name__ == "__main__":
    build_index_analysis()


