#!/usr/bin/env python


#http://www.renesys.com/challenge_site/challenge/bowlarama
#
# The ANSWER to this challenge is the MEAN AVERAGE (i.e., weighted
# sum of scores / n) of all bowling games in the file, rounded to
# the nearest hundredth (example: 141.34).

from __future__ import print_function


import argparse
import sys
from itertools import count



class Spare(object):

    def __init__(self, first):
        self.first = first
        self.second = 10 - first


    def __repr__(self):
        return 'Spare object: {}, {}'.format(self.first, self.second)




class Strike(object):

    def __init__(self):
        pass



class Throw(object):


    def __init__(self, first, second, bonus=(1, 1)):
        self.first = first
        self.second = second
        self.bonus = bonus


    def __add__(self, other):
        if isinstance(other, Throw):
            return Throw(self.bonus[0] * (self.first + other.first),
                         self.bonus[1] * (self.second + other.second))
        elif isinstance(other, Spare):
            return Throw(self.bonus[0] * (self.first + other.first),
                         self.bonus[1] * (self.second + other.second),
                         (2, 1))
        else:
            return NotImplemented


    def __repr__(self):
        return 'Throw object: {}, {}'.format(self.first, self.second)



def game(line):
    line = iter(line.strip('-'))
    step = 0
    while True:
        try:
            first = int(next(line))
            try:
                second = int(next(line))
                yield Throw(first, second)
            except StopIteration:
                yield Throw(first, 0)
            except ValueError:
                yield Spare(first)
        except ValueError:
            yield Strike()



def main(args):
    # for line in args.input:
    #     line = line.strip()
    #     print(list(game(line)))
    for pat in ['1/2/3/4/5/6/7/8/9/5/5', '01532790334561118100-']:
        print(sum(game(pat), Throw(0, 0)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                        default=sys.stdin)
    main(parser.parse_args())
