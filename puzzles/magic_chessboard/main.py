"""
    Sandbox :: main
        created by Marcus LJX on 2016-07-07
"""

import numpy as np

BOARDSIZE = 8


def init_puzzle_board():
    return np.random.randint(2, size=(BOARDSIZE, BOARDSIZE)), np.random.randint(BOARDSIZE, size=2)


def main():
    pass


if __name__ == '__main__':
    main()
