__author__ = 'jesse'


def create_ngrams(traj, n):
    tuples = []
    for i in range(n, len(traj)):
        f = i - n
        e = n
        tuples.append(traj[f:e])
    return tuples