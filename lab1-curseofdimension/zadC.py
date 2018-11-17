import scipy
import numpy
from random import random


points_number = 500


def zad_c(dim):
    angles = []
    point_list = []
    for i in range(points_number):
        point = []
        for j in range(0, dim):
            point.append(random())
        point_list.append(point)

    vectors = []
    points_num = points_number
    for i in range(2):
        x = int(random() * points_num)
        y = int(random() * (points_num - 1))
        point_x = numpy.asarray(point_list[x])
        point_list.pop(x)
        point_y = numpy.asarray(point_list[y])
        point_list.pop(y)

        vector = point_y - point_x
        vectors.append(vector)
        points_num = points_number - 2


    #print(vectors)

    # cos(angle) = (dot_product/len(a)/len(b)
    x = numpy.float64(numpy.linalg.norm(vectors[0]))*numpy.float64(numpy.linalg.norm(vectors[1]))
    #print("eeeee ", numpy.linalg.norm(vectors[0]), numpy.linalg.norm(vectors[1]))
    #print(x)
    cos_angle = numpy.dot(vectors[0], vectors[1])/x
    angle = numpy.arccos(numpy.clip(cos_angle, -1, 1))
    print(angle)
    return angle

