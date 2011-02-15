#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback


def is_pandigital(number):
    return len(number) == 9 and len(set(number)) == 9 and '0' not in number



def produce(limit):
    for number in xrange(limit):
        for multiplier_limit in xrange(3, 8):
            concat = ''.join(str(number * multiplier)
                             for multiplier in xrange(1, multiplier_limit))
            if is_pandigital(concat):
                yield int(concat), number



def process(args):
    try:
        print max(produce(args.limit))
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
    parser.add_argument('-l', '--limit', default=100, type=int)
    main(parser.parse_args())
