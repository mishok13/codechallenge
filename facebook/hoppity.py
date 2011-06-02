#!/usr/bin/env python


import sys



def main(fname):
    limit = int(open(fname).read().strip())
    for x in xrange(1, limit + 1):
        if not x % 15:
            print 'Hop'
            continue
        if not x % 3:
            print 'Hoppity'
        if not x % 5:
            print 'Hophop'



if __name__ == '__main__':
    main(sys.argv[1])
