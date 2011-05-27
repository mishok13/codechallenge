#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from itertools import product, chain, ifilter, imap
from collections import defaultdict
import cPickle as pickle


available = [1, 2, 5, 10, 20, 50, 100, 200]


def solve(value, cache=None):
    if cache is None:
        cache = {0: [], 1: set([(1, )]),
                 2: set([(1, 1), (2, )])
                 }
    def solver(val):
        try:
            return cache[val]
        except KeyError:
            solution = set()
            for coin in available:
                if coin < val:
                    for left, right in product(solver(val - coin), solver(coin)):
                        solution.add(tuple(sorted(left + right)))
                elif coin == val:
                    solution.add((coin, ))
            cache[val] = solution
            return solution
    return solver(value), cache


def main(args):
    try:
        with open(args.cache) as cachefile:
            cache = pickle.load(cachefile)
    except IOError:
        cache = None
    ret, cache = solve(args.value, cache)
    with open(args.cache, 'w') as cachefile:
        pickle.dump(cache, cachefile)
    print len(ret)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--value', default=200, type=int)
    parser.add_argument('-c', '--cache', default='cache.db')
    main(parser.parse_args())
