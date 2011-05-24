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


def solution(anagrams):
    for key, words in anagrams:
        for variant in find_squares(key):
            table = dict(zip(words[0], variant))
            if ''.join(table[c] for c in words[1]) in squares:
                yield int(''.join(variant))
            table = dict(zip(words[1], variant))
            if ''.join(table[c] for c in words[0]) in squares:
                yield int(''.join(variant))




def main(args):
    anagrams = defaultdict(list)
    for word in args.input.read().split(','):
        word = word.strip('"')
        anagrams[tuple(sorted(word))].append(word)
    # We only have one case where there're 3 anagrams and it only
    # contains 4-letter words, so we can safely ignore this case here
    print max(solution((key, words) for key, words in anagrams.iteritems()
                       if len(words) == 2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default=open('words.txt'),
                        type=argparse.FileType('r'))
    main(parser.parse_args())
