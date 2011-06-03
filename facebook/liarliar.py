#!/usr/bin/env python



import sys



def main(fname):
    # The task actually is solved by assuming that the resulting
    # relationship graph is bipartite
    # The actual definition is right there at Wikipedia:
    # """
    # If a bipartite graph is connected, its bipartition can be
    # defined by the parity of the distances from any arbitrarily
    # chosen vertex v: one subset consists of the vertices at even
    # distance to v and the other subset consists of the vertices
    # at odd distance to v.
    # """
    # So the task is simply to build a graph, randomly pick vertex
    # and calculate the distances to all other vertices
    # This sounds doable even in pure Python, though I'm concerned
    # about the memory usage. __slots__ to the resque maybe?
    pass



if __name__ == '__main__':
    main(sys.argv[1])
