import numpy as np


def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = np.sqrt((x2-x1)**2 +(y2-y1)**2)
    return d


def get_sensors_distances(p, s_list):
    d_list = []
    for sensor in s_list:
        d_list.append(get_distance(p, sensor))
    return d_list


if __name__ == '__main__':
    print("navigato started")
    # set room
    # sensors
    s1 = (0, 0)
    s2 = (2, 2)
    s3 = (0, 4)

    # beacom
    p = (2, 1)

    d_list = get_sensors_distances(p, [s1, s2, s3])
    print(d_list)
