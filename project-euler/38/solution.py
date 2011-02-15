#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback


def process(args):
    try:
        raise NotImplementedError
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
