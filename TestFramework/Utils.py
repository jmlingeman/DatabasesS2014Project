__author__ = 'jesse'

import numpy


def create_ngrams(traj, n):
    tuples = []
    if len(traj) >= n:
        for i in range(n, len(traj)):
            f = i - n
            e = i
            tuples.append(traj[f:e])
    return tuples


def calc_stats(reads, writes):
    reads_std = numpy.std(reads)
    writes_std = numpy.std(writes)
    reads_avg = numpy.mean(reads)
    writes_avg = numpy.mean(writes)

    stats = {
        "Average Reads": reads_avg,
        "Average Writes": writes_avg,
        "STD of Reads": reads_std,
        "STD of Writes": writes_std,
        "Maximum Reads": max(reads),
        "Minimum Reads": min(reads),
        "Maximum Writes": max(writes),
        "Minimum Writes": min(writes),
        "Total Writes": sum(writes),
        "Total Reads": sum(reads)
    }
    return stats