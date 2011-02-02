#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from operator import itemgetter


def consecutives(table, width, height):
    for row in xrange(height):
        yield [table[(row, column)] for column in xrange(width)]
    for column in xrange(height):
        yield [table[(row, column)] for row in xrange(height)]
    for row in xrange(height):
        yield [table[(column + row, column)] for column in xrange(width - row)]
    for column in xrange(width):
        yield [table[(row, row + column)] for row in xrange(height - column)]
    for row in xrange(height):
        yield [table[(row - column, column)] for column in xrange(row + 1)]
    for column in xrange(width):
        yield [table[(height - 1 - row, column + row)] for row in xrange(width - column)]

def process(args):
    try:
        table = {}
        for row, line in enumerate(args.input):
            for column, number in enumerate(map(int, line.strip().split())):
                table[(row, column)] = number
        width, height = max(table.keys())
        for consecutive in consecutives(table, width + 1, height + 1):
            print consecutive
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
    parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('-l', '--length', type=int, default=4)
    main(parser.parse_args())
