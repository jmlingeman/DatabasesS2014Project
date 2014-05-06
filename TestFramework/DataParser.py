__author__ = 'jesse'


def read_trajectory_data(input_file):
    input_file = open(input_file, 'r')
    data = []
    for line in input_file:
        id = line[:len("./dOxIc2o4o8zutl9hXW.M")]
        traj = line[len("./dOxIc2o4o8zutl9hXW.M") + 1:].strip()
        traj = traj.split(",")
        data.append([id, traj])

    # Go through the data and build a hash for each ID
    id_to_num = {}
    num_to_id = {}
    for i, d in enumerate(data):
        id_to_num[d[0]] = i
        num_to_id[i] = d[0]
        d[0] = i
    print data[0]
    print len(data)

    # Now get the list of names and build a map of those in alphabetical order
    names = set()
    # print data[0][1]
    for d in data:
        for t in d[1]:
            names.add(t)
    names = list(names)
    names.sort()

    pid_to_place = {}
    place_to_pid = {}
    for i, d in enumerate(data):
        pid_to_place[d[0]] = i
        place_to_pid[i] = d[0]

    return data, names, id_to_num, num_to_id, pid_to_place, place_to_pid