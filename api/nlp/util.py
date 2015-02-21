#!/usr/bin/env python
def flatten(l):
    from itertools import chain
    return list(chain.from_iterable(l))

def uniq(l):
    return list(set(l))


if __name__ == '__main__':
    l = [[1, 2, 3], [4, 5], [5, 6], [6, 7, 8]]
    print l

    f_l = flatten(l)
    print f_l

    u_l = uniq(f_l)
    print u_l


    
