import sys
import os
import math


def distance(n1, n2):
    if n1*n2 < 0:
        return math.fabs(n1 + n2)
    else:
        return math.fabs(n1 - n2)

x1 = 1
x2 = 2
print("{},{} distance is {}".format(x1, x2, distance(x1, x2)))

x1 = -1
x2 = -2
print("{},{} distance is {}".format(x1, x2, distance(x1, x2)))

x1 = 1
x2 = -2
print("{},{} distance is {}".format(x1, x2, distance(x1, x2)))

x1 = -10
x2 = 10

while (x1 < x2):
    print("{},{} distance is {}".format(x1, x2, distance(x1, x2)))
    x1 += 1
    x2 -= 0.5


for i in range(0, 100):
    print("{} power 2 results in {}".format(i, math.floor(math.pow(i, 2))))




