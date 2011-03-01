#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback


def process(args):
    try:
        count = int(args.input.readline())
        for index, line in enumerate(args.input, 1):
            quantity, snaps = map(int, line.strip().split())
            if (snaps + 1) % (2**quantity) == 0:
                print "Case #%d: ON" % index
            else:
                print "Case #%d: OFF" % index
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
    parser.add_argument('input', type=argparse.FileType('r'))
    main(parser.parse_args())
