#!/usr/bin/env python


import argparse
from collections import defaultdict
from itertools import permutations
from math import sqrt


numbers = map(str, range(10))
squares = set(str(x**2) for x in xrange(int(sqrt(9876543210)) + 2))


def find_squares(word):
    for variant in permutations(numbers, len(word)):
        number = ''.join(variant)
        if number in squares:
            yield variant


def main(args):
    anagrams = defaultdict(list)
    for word in args.input.read().split(','):
        word = word.strip('"')
        anagrams[tuple(sorted(word))].append(word)
    for key, value in anagrams.iteritems():
        # We only have one case where there're 3 anagrams, so
        # let's ignore it for now
        if len(value) == 2:
            print key, value
            for variant in find_squares(key):
                pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default=open('words.txt'),
                        type=argparse.FileType('r'))
    main(parser.parse_args())
