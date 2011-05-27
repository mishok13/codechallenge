#!/usr/bin/env python


import argparse
import gmpy
from math import ceil



def gen():
    step = 2
    start = 1
    yield start
    while True:
        for _ in xrange(4):
            start = start + step
            yield start
        step += 2


def main(args):
    primes = 0
    for count, number in enumerate(gen()):
        if gmpy.is_prime(number):
            primes += 1
        if primes:
            if float(primes) / count <= args.ratio:
                print number, primes, count, int(ceil(count / 4.0) * 2 + 1)
                break



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--ratio', default=0.6, type=float)
    main(parser.parse_args())
