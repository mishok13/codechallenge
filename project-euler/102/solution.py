#!/usr/bin/env python



import argparse
from shapely.geometry import Polygon, Point
import sys



def main(args):
    origin = Point(0, 0)
    print sum(Polygon(zip(*([iter(map(int, line.strip().split(',')))] * 2))).intersects(origin) for line in args.input)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    main(parser.parse_args())
