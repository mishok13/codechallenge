#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback


def routes(size, route):
    point = route[-1]
    if point == (size, size):
        return route
    if point[0] != size:
         routes(size, (point[0] + 1, point[1]))
    if point[1] != size:
        return routes(size, (point[0], point[1] + 1))


def process(args):
    try:
        print routes(args.size, [(0, 0)])
    except Exception:
        traceback.print_exc()
        return 2
    except BaseException:
        traceback.print_exc()
        return 1


def main(args):
    sys.exit(process(args))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', default=2, type=int)
    main(parser.parse_args())
