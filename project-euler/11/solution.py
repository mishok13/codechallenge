#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback


def print_consecutives(table):
    raise NotImplementedError


def process(args):
    try:
        table = {}
        for row, line in enumerate(args.input):
            for column, number in enumerate(map(int, line.strip().split())):
                table[(row, column)] = number
        print_consecutives(table)
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
