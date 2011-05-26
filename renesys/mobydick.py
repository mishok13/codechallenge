#!/usr/bin/env python

from __future__ import print_function


import argparse
import sys
from itertools import islice, ifilter
from collections import defaultdict, Counter
from string import ascii_lowercase
from operator import itemgetter

ascii_lowercase = set(ascii_lowercase)
vowels = set('aeiou')
consonants = ascii_lowercase - vowels


def is_cvvc(word):
    for x in xrange(len(word) - 3):
        try:
            if word[x] in consonants and\
               word[x + 1] in vowels and\
               word[x + 2] in vowels and\
               word[x + 3] in consonants:
                return True
        except IndexError:
            return False
    return False



def gen_words(lines):
    for line in lines:
        for word in line.split():
            # ifilter(ascii_lowercase.__contains__, word.lower()) he-he
            word = ''.join(char for char in word.lower() if char in ascii_lowercase)
            if is_cvvc(word):
                yield word


def main(args):
    lines = (line.strip().replace('--', ' -- ')
             for line in islice(args.input, 30, 21746))
    counter = Counter(gen_words(lines))
    res = dict((word[0], index) for index, word in
               enumerate(sorted(counter.iteritems(), key=itemgetter(1), reverse=True), 1))
    print(res['ishmael'] + res['queequeg'])



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                        default=sys.stdin)
    main(parser.parse_args())
