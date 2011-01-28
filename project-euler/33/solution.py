#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from fractions import Fraction


def process(args):
    try:
        product = Fraction(1, 1)
        for numerator in xrange(10, 99):
            for denominator in xrange(numerator + 1, 100):
                num, den = int(str(numerator)[0]), int(str(denominator)[1])
                if (str(numerator)[1] == str(denominator)[0] and num < den and
                    Fraction(numerator, denominator) == Fraction(num, den)):
                    product *= Fraction(num, den)
                    print (numerator, denominator), (num, den)
        print product
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
