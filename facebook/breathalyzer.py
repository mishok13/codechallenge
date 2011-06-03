#!/usr/bin/env python


import sys



def word_slice(word):
    for index, char in enumerate(word):
        yield word[:index], char, word[index + 1:]



def levdis(first, second):
    previous = zip(first, xrange(len(first)))
    current = zip(first, xrange(len(first)))
    first = ' ' + first
    for char in second:
        pass
    print(zip(first, xrange(len(first))))
    print(zip(second, xrange(len(second))))



def levenstein_distance(first, second):
    cache = dict(((i, j), 0) for i in xrange(len(first)) for j in xrange(len(second)))
    for i, fchar in enumerate(first):
        for j, schar in enumerate(second):
            if fchar == schar:
                cache[(i, j)] = cache.get((i - 1, j - 1), 0)
            else:
                cache[(i, j)] = current = min(cache.get((i - 1, j), 0),
                                              cache.get((i, j - 1), 0),
                                              cache.get((i - 1, j - 1), 0)) + 1

    print current



def main():
    levdis('kitten', 'sitting')
    levdis('Sunday', 'Saturday')



if __name__ == '__main__':
    main()
