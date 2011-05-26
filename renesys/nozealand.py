#!/usr/bin/env python

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
    print(sorted(net for loc, nets in networks.iteritems() if 10 < len(nets) < 100 for net in nets)[9999])
    # for loc, nets in networks.iteritems():
    #     if 10 < len(nets) < 99:
    #         print(loc, len(nets), sorted(nets))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                        default=sys.stdin)
    main(parser.parse_args())
