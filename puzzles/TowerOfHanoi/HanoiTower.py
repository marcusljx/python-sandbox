""" Sandbox :: HanoiTower

Description:
    Class for emulating the tower of hanoi

Author:
    marcusljx

Created:
    2016-07-08

Doctests:
>>> H = HanoiTower(16)
>>> H.swap(0, 2, 2)
>>> H.recursive_shift()
>>> print(H)
array([[ 0,  0,  1],
       [ 0,  0,  2],
       [ 0,  0,  3],
       [ 0,  0,  4],
       [ 0,  0,  5],
       [ 0,  0,  6],
       [ 0,  0,  7],
       [ 0,  0,  8],
       [ 0,  0,  9],
       [ 0,  0, 10],
       [ 0,  0, 11],
       [ 0,  0, 12],
       [ 0,  0, 13],
       [ 0,  0, 14],
       [ 0,  0, 15],
       [ 0,  0, 16]])
"""
import numpy as np


class HanoiTower():
    def __init__(self, N):
        self.board = np.zeros((N, 3), dtype=int)
        for i in range(N):
            self.board[i][0] = i + 1

        self.total_steps = 0

    def swap(self, pegA, pegB, level):
        temp = self.board[level][pegB]
        self.board[level][pegB] = self.board[level][pegA]
        self.board[level][pegA] = temp

    def recursive_shift(self, start=0, end=2, considering_limit=None):
        if considering_limit == 1:
            self.swap(start, end, 0)

        else:
            if not considering_limit:
                considering_limit = self.board.shape[0]

            # find spare
            mid = [i for i in [0, 1, 2] if i not in [start, end]][0]

            # move all except base
            self.recursive_shift(start, mid, considering_limit - 1)

            # move base
            self.swap(start, end, considering_limit - 1)

            # move all to base
            self.recursive_shift(mid, end, considering_limit - 1)

    def show_stage(self):
        self.total_steps += 1
        print("\n=== Step %s ===" % '{0:6}'.format(self.total_steps))
        # print(self.board)

    def __str__(self):
        return repr(self.board)
