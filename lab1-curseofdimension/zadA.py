import scipy
import numpy
from random import random


points_num = 500
radius = 1


def zad_a(n):
    # print("dimension: ", n)
    ilen = 0                        # punkty które pasują
    for i in range(points_num):     #
        p = []                      # tablica z wartościami dla wszystkich wymiarów
        for j in range(n):          #
            x = random()*2-1        # losujemy j wymiarów
            p.append(x)             #
        q = map(lambda x: x**2, p)  #do kwadratu
        w = sum(q)
        e = w**0.5
        if e <= radius:
            ilen += 1
    result = (ilen/points_num) * 100
    # print("result: ", ilen/points_num)
    # print(result)
    return result

