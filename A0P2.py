# -*- coding: utf-8 -*-
from more_itertools import powerset

if __name__ == '__main__':
    U = set(range(5))
    V = {'a', 'b', 'c', 'd', 'e'}
    W = set((x, y) for x in U for y in V)
    Pv = set(powerset(V))
    print(W)
    print(len(W))
    print(Pv)
    print(len(Pv))

