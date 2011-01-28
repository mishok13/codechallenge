#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback


def pandigital():
    cache = set()
    for multiplicand in xrange(1, 10000):
        for multiplier in xrange(1, (999999 / multiplicand) + 2):
            number = multiplicand * multiplier
            string = ''.join(map(str, (multiplicand, multiplier, number)))
            if len(string) == 9:
                string = set(string)
                if '0' not in string and len(string) == 9:
                    if number not in cache:
                        cache.add(number)
                        yield number


def process(args):
    try:
        print sum(pandigital())
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
    main(parser.parse_args())
