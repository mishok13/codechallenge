#!/usr/bin/env python


from fractions import Fraction as F
from math import sqrt, floor, ceil
from itertools import count



GOAL = sqrt(1 / 2.0)


def main():
    for y in count(10**12):
        x = int(y * GOAL) + 1
        if F(x, y) * F(x - 1, y - 1) == F(1, 2):
            print x, y


if __name__ == '__main__':
    main()
