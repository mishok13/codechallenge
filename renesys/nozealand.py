#!/usr/bin/env python

# The task itself:
#
# A customer is interested in a particular subset of
# the networks in that file. Find the networks that interest them.
#
#     * They only care about networks in locations having more than
#     10 but fewer than 100 networks (or 11-99, inclusive)
#
#     * A location is a distinct tuple of (country,region,city) --
#     parts can be empty. E.g., ('US',None,None) is a different
#     place than ('US','MA','Boston') and neither contains the
#     other. If it doubt, stick to the simple interpretation of
#     locations as tuples (where None is a valid value).
#     * Exclude all locations in New Zealand (NZ), Belgium (BE),
#     or the state of Hawaii (HI).
#
#     * Sort all distinct networks from these locations
#     lexicographically (as strings, using C Locale ordering).
#
#     * Take the 10,000th network (1-indexed -- the 'first' element
#     in the list is element 1)
#
#     * Enter the network (as a string), your email, and your
#     code into the form below and submit it.


from __future__ import print_function



import argparse
from collections import defaultdict
import sys



def main(args):
    networks = defaultdict(set)
    for line in args.input:
        network, source, country, region, city, score = line.strip().split('\t')
        if country not in ('NZ', 'BE') and (country, region) != ('US', 'HI'):
            networks[(country, region, city)].add(network)
    print(sorted(net for loc, nets in networks.iteritems()
                 if 10 < len(nets) < 100 for net in nets)[9999])



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                        default=sys.stdin)
    main(parser.parse_args())
