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
        "reads_avg": reads_avg,
        "writes_avg": writes_avg,
        "reads_std": reads_std,
        "writes_std": writes_std,
        "reads_max": max(reads),
        "reads_min": min(reads),
        "writes_max": max(writes),
        "writes_min": min(writes)
    }
    return stats