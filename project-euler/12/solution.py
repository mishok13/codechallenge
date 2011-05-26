#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from itertools import islice, count


def triangles():
    current = 0
    for step in count(1):
        current += step
        yield current


def divisors(number, cache={1: set([1])}):
    # Number itself and 1 are already divisors
    try:
        return cache[number]
    except KeyError:
        ret = set([1, number])
        for divisor in xrange(number / 2, 1, -1):
            if number % divisor == 0:
                ret |= divisors(divisor) | divisors(number / divisor)
        cache[number] = ret
        return ret


def process(args):
    try:
        for number in islice(triangles(), args.skip, args.skip + args.limit):
            number_divisors = len(divisors(number))
            if number_divisors >= args.divisors:
                print number, number_divisors
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
    parser.add_argument('-d', '--divisors', default=10, type=int)
    parser.add_argument('-l', '--limit', default=100, type=int)
    parser.add_argument('-s', '--skip', default=0, type=int)
    main(parser.parse_args())
