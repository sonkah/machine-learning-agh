from random import random
from scipy.spatial import distance
import numpy

points_num = 100
pairs_num = 50


def zad_b(dim):
    # sześcian wypełniony losowo punktami
    point_list = []
    for i in range(points_num):
        point = []
        for j in range(0, dim):
            point.append(random())
        point_list.append(point)
        #print(i)
    #print(point_list)

    #print("************")
    dis_array = []
    for i in range(0, len(point_list)):  # dla punktu
        for j in range(i + 1, len(point_list)):  #
            p = point_list[i]
            q = point_list[j]
            dst = distance.euclidean(p, q)
            dis_array.append(dst)

    avg = numpy.mean(dis_array)
    std_dev = numpy.std(dis_array)
    #print("srednia: ", avg)
    print("odchylenie: ", std_dev)
    return std_dev/avg





