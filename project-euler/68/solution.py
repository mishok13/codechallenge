#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from itertools import combinations, permutations


def candidates():
    seed = set(range(1, 11))
    for outer in permutations(seed, 5):
        outer = list(outer)
        if 10 not in set(outer):
            continue
        inner = seed - set(outer)
        for inner_variant in permutations(inner, 5):
            yield outer, list(selection(inner_variant))


def selection(numbers):
    for index in xrange(len(numbers) - 1):
        yield numbers[index], numbers[index + 1]
    yield numbers[0], numbers[-1]



def condition(outer, inner):
    sums = [line[0] + sum(line[1]) for line in zip(outer, inner)]
    for sum_ in sums[1:]:
        if sum_ != sums[0]:
            return False
    return True


def number(outer, inner):
    #TODO:kill me for this
    # int call to make sure it's an integer, haha
    return int(''.join([''.join(map(str, (num[0], num[1][0], num[1][1]))) for num in sorted(zip(outer, inner))]))


def process(args):
    try:
        print max(number(outer, inner) for outer, inner in candidates() if condition(outer, inner))
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
