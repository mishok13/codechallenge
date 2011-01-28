#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback


def totient(n):
    return sum(1 for x in xrange(1, n) if n % x) + 1


def process(args):
    try:
        print [(n, totient(n)) for n in xrange(2, args.limit)]
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
