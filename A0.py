# -*- coding: utf-8 -*-
"""
Assignment 0 template

For submission, rename this file to "A0.py" 

Answer each question in the corresponding method definition stub below
"""

VALID_MOVES = {
    0: {(1, 'R'), (3, 'D')},
    1: {(0, 'L'), (2, 'R'), (4, 'D')},
    2: {(1, 'L'), (5, 'D')},
    3: {(0, 'U'), (4, 'R'), (6, 'D')},
    4: {(3, 'L'), (1, 'U'), (5, 'R'), (7, 'D')},
    5: {(5, 'L'), (2, 'U'), (8, 'D')},
    6: {(3, 'U'), (7, 'R')},
    7: {(6, 'L'), (4, 'U'), (8, 'R')},
    8: {(7, 'L'), (5, 'U')}
}

def Q1(A, B):
    union = A.union(B)
    intersection = A.intersection(B)
    return union, intersection


def Q2(A, B):
    isdisjoint = A.isdisjoint(B)
    if isdisjoint:
        return 'DISJOINT'
    else:
        return 'INTERSECTING'


def Q3(a, b):
    X = set()
    for i in range(a):
        X.add(i)
    Y = set()
    for i in range(b):
        Y.add(i)
    G = set()
    for x in X:
        for y in Y:
            G.add((x, y))
    return X, Y, G


def Q4(E, n):
    n_successors = set()
    for element in E:
        edge = E[element]
        if edge[0] == n:
            n_successors.add(edge[1])
    return n_successors


def Q5(inFile, outFile, remove):
    inputHandler = open(inFile, 'r')
    inputText = inputHandler.read()
    inputText = inputText.replace(remove, '')
    output = open(outFile, 'w')
    output.write(inputText)
    print('Character ' + remove + ' removed from ' + inFile)
    print('Output written to ' + outFile)

def ValidStates(state1, state2, index1, index2):
    if (len(state1) != 9 or len(state2) != 9
            or state1.count('_') != 1 or state2.count('_') != 1):
        return False
    shiftedCell = state2[index1]
    if (shiftedCell != state1[index2]):
        return False
    for i in range(9):
        if (i != index1 and i != index2):
            if (state1[i] != state2[i]):
                return False
    return True

def GetMove(index1, index2):
    for (key, value) in VALID_MOVES.get(index1):
        if index2 == key:
            return value
    return None

def Q6(state1, state2):
    index1 = state1.find('_')
    index2 = state2.find('_')
    if not ValidStates(state1, state2, index1, index2):
        print('IMPOSSIBLE')
        return
    move = GetMove(index1, index2)
    if move is None:
        print('IMPOSSIBLE')
        return
    print(move)
