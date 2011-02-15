#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
import gmpy
from collections import defaultdict
from itertools import islice, dropwhile, imap, ifilter



def primes(limit):
    prime = 2
    while prime < limit:
        yield prime
        prime = gmpy.next_prime(prime)



def divide(dividend, divisor):
    remainder = dividend
    while remainder:
        quotient = dividend / divisor
        remainder = dividend - quotient * divisor
        dividend = remainder * 10
        yield quotient



def recurrence(producer):
    number = []
    for digit in producer:
        number.append(digit)
        for limit in xrange(1, len(number) / 3):
            if number[:limit] == number[limit:limit*2] == number[limit * 2:limit * 3]:
                return len(''.join(map(str, number[:limit])))
    return 0


def solve(limit):
    for prime in primes(limit):
        rec = recurrence(dropwhile(lambda num: num == 0, divide(1, prime)))
        print rec, int(prime)
        yield rec, int(prime)



def process(args):
    try:
        print max(solve(args.limit))
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
    parser.add_argument('-l', '--limit', type=int, default=1000)
    main(parser.parse_args())
