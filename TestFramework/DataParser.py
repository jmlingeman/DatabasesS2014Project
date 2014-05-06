__author__ = 'jesse'


def read_trajectory_data(input_file):
    input_file = open(input_file, 'r')
    data = []
    for line in input_file:
        id = line[:len("./dOxIc2o4o8zutl9hXW.M")]
        traj = line[len("./dOxIc2o4o8zutl9hXW.M") + 1:].strip()
        traj = traj.split(",")
        data.append([id, traj])
    return data