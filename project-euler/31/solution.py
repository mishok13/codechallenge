#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from itertools import product, chain, ifilter
from collections import defaultdict


available = [1, 2, 5, 10, 20, 50, 100, 200]


def solve(maximum):
    cache = defaultdict(list)
    def solver(value, coins):
        res = []
        for coin in available:
            if coin == value:
                res.append(tuple(sorted(coins + [coin])))
            elif coin < value:
                solution = solver(value - coin, coins + [coin])
                if solution:
                    res.extend(solution)
        ret = tuple(set(res))
        cache[sum(coins)].append(ret)
        return ret
    return solver(maximum, []), cache


def solve_working(maximum):
    cache = {}
    def solver(value, coins):
        try:
            return cache[value]
        except KeyError:
            res = []
            for coin in available:
                if coin == value:
                    res.append(tuple(sorted(coins + [coin])))
                elif coin < value:
                    solution = solver(value - coin, coins + [coin])
                    if solution:
                        res.extend(solution)
            ret = list(set(res))
            # cache[value] = ret
            return ret
        # for solution in ifilter(None, (solver(value - coin, coins + [coin]) if value - coin else coins + [coin] for coin in available if coin <= value)):
        #     print value, sorted(solution)
    return solver(maximum, [])


def main(args):
    ret = solve(args.value)
    print ret


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--value', default=200, type=int)
    main(parser.parse_args())
