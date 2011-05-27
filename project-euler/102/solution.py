#!/usr/bin/env python


from math import sqrt


def semiperimeter(a, b, c):
    return sum([a, b, c]) / 2.0


def heron(a, b, c):
    s = semiperimeter(a, b, c)
    return sqrt(s * (s - a) * (s - b) * (s -c))


def side(first, second):
    return sqrt((first[0] - second[0])**2 + (first[1] - second[1])**2)


def main():
    points = [(-340,495), (-153,-910), (835,-947)]
    outer = [side(points[0], points[1]), side(points[1], points[2]), side(points[2], points[0])]
    print outer, heron(*outer)
    sides = [side((0, 0), point) for point in points]
    print heron(sides[0], sides[1], outer[0]) + heron(sides[1], sides[2], outer[1]) + heron(sides[2], sides[0], outer[2])



if __name__ == '__main__':
    main()
