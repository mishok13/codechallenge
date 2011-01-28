#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import traceback
from collections import defaultdict


class Unmatched(Exception):
    pass


def royal_flush(hand):
    """Check if the hand is a Royal Flush"""
    flush(hand)
    straight(hand)
    if max(hand.values) == 12:
        return (9, ())
    else:
        raise Unmatched



def straight_flush(hand):
    """Check if the hand is a Straight Flush"""
    flush(hand)
    straight(hand)
    return (8, (max(hand.values), ))



def four(hand):
    """Check if the hand is Four of a Kind"""
    values = set(hand.values)
    for value in values:
        if hand.values.count(value) == 4:
            values.discard(value)
            return (7, (value, values.pop()))
    raise Unmatched


def full_house(hand):
    """Check the hand for Full House"""
    values = set(hand.values)
    if len(values) == 2 and hand.values.count(hand.values[0]) in (2, 3):
        threes = (value for value in values if hand.values.count(value) == 3).next()
        twos = (value for value in values if hand.values.count(value) == 2).next()
        return (6, (threes, twos))
    else:
        raise Unmatched


def flush(hand):
    if len(set(hand.colors)) == 1:
        return (5, tuple(sorted(hand.values, reverse=True)))
    raise Unmatched


def straight(hand):
    values = iter(sorted(hand.values))
    previous = values.next()
    for current in values:
        if current - previous != 1:
            raise Unmatched
        previous = current
    return (4, max(hand.values))


def three(hand):
    values = defaultdict(int)
    for value in hand.values:
        values[value] += 1
    if any(value == 3 for value in values.values()):
        return (3, tuple(sorted(values, key=lambda k: (values[k], k), reverse=True)))
    raise Unmatched


def two_pairs(hand):
    values = defaultdict(int)
    for value in hand.values:
        values[value] += 1
    if len(values) == 3:
        return (2, tuple(sorted(values, key=lambda k: (values[k], k), reverse=True)))
    raise Unmatched


def pair(hand):
    values = defaultdict(int)
    for value in hand.values:
        values[value] += 1
    if len(values) == 4:
        return (1, tuple(sorted(values, key=lambda k: (values[k], k), reverse=True)))
    raise Unmatched


def highcard(hand):
    return (0, tuple(sorted(hand.values, reverse=True)))


class Hand(object):

    def __init__(self, cards):
        self.cards = map(Card, cards)
        self.values = [card.value for card in self.cards]
        self.colors = [card.color for card in self.cards]
        self.patterns = [royal_flush, straight_flush, four, full_house, flush,
                         straight, three, two_pairs, pair, highcard]
        for pattern in self.patterns:
            try:
                self.pattern = pattern(self)
                break
            except Unmatched:
                continue


class Card(object):

    values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
              '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

    def __init__(self, card):
        self.value = self.values[card[0]]
        self.color = card[1]

    def __repr__(self):
        return repr((self.value, self.color))


def process(args):
    try:
        print sum(Hand(cards[:5]).pattern > Hand(cards[5:]).pattern for cards in
                  (line.split() for line in args.input))
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
    parser.add_argument('-i', '--input', default=sys.stdin,
                        type=argparse.FileType('r'))
    main(parser.parse_args())
