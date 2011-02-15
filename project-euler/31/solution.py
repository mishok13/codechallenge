#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from itertools import product


values = [1, 2, 5, 10, 20, 50, 100, 200]



def process(args):
    try:
        print map(xrange, (args.value / value for value in values))
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
    parser.add_argument('-v', '--value', default=200, type=int)
    main(parser.parse_args())
