__author__ = 'jesse'


def create_ngrams(traj, n):
    tuples = []
    if len(traj) >= n:
        for i in range(n, len(traj)):
            f = i - n
            e = i
            tuples.append(traj[f:e])
    return tuples