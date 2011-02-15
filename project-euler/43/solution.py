#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from itertools import permutations
from gmpy import next_prime


def produce_checkers(limit=7):
    prime = 1
    for start in xrange(limit):
        prime = next_prime(prime)
        yield slice(start + 1, start + 4), prime


def produce():
    checkers = list(reversed(list(produce_checkers())))
    for number in permutations('0123456789'):
        for slice_, divisor in checkers:
            if int(''.join(number[slice_])) % divisor:
                break
        else:
            yield int(''.join(number))


def process(args):
    try:
        print sum(produce())
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
